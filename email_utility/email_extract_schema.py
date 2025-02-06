from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import List, Optional
from datetime import datetime

# Metadata view: Contains sender, recipient, and other header information.
class EmailMetadata(BaseModel):
    sender: str = Field(..., description="The sender's email address")
    recipients: List[EmailStr] = Field(..., description="List of recipient email addresses")
    cc: Optional[List[EmailStr]] = Field(default_factory=list, description="List of CC email addresses")
    bcc: Optional[List[EmailStr]] = Field(default_factory=list, description="List of BCC email addresses")
    timestamp: datetime = Field(..., description="The date and time when the email was sent")
    subject: str = Field(..., description="Subject line of the email")
    message_id: str = Field(..., description="Unique message identifier for the email")

# Content view: Represents the main body content and any embedded links or signatures.
class EmailContent(BaseModel):
    text: Optional[str] = Field(None, description="Plain text version of the email body")
    html: Optional[str] = Field(None, description="HTML version of the email body")
    links: Optional[List[HttpUrl]] = Field(default_factory=list, description="Any embedded URLs found in the content")
    signature: Optional[str] = Field(None, description="Extracted signature block, if present")

# Attachment view: Details about files attached to the email.
class Attachment(BaseModel):
    filename: str = Field(..., description="Name of the attachment file")
    filetype: str = Field(..., description="MIME type or file extension of the attachment")
    filesize: int = Field(..., description="Size of the file in bytes")
    url: Optional[HttpUrl] = Field(None, description="URL to access the attachment, if applicable")

# Thread/Conversation view: Information to reconstruct the conversation.
class EmailThread(BaseModel):
    in_reply_to: Optional[str] = Field(None, description="Message-ID this email is replying to")
    references: Optional[List[str]] = Field(default_factory=list, description="List of Message-IDs referenced in the conversation")

# Transaction or policy data view: Extract any transaction-specific data.
class TransactionData(BaseModel):
    policy_number: Optional[str] = Field(None, description="Policy number extracted from the email content")
    claim_id: Optional[str] = Field(None, description="Claim identifier, if applicable")
    transaction_amount: Optional[float] = Field(None, description="Monetary value mentioned in the email, if any")

# Compliance view: Markers for regulatory, confidentiality or keyword analysis.
class ComplianceData(BaseModel):
    keywords: Optional[List[str]] = Field(default_factory=list, description="List of compliance or trigger keywords found")
    confidentiality: bool = Field(False, description="Indicator if the email is marked as confidential")

# Action Items / Follow-up view: Tasks or instructions extracted from the email.
class ActionItem(BaseModel):
    description: str = Field(..., description="Description of the action item or follow-up task")
    deadline: Optional[datetime] = Field(None, description="Deadline for the action item, if mentioned")

# Main schema: Combines all views into one comprehensive email extraction model.
class EmailExtract(BaseModel):
    metadata: EmailMetadata = Field(..., description="Metadata extracted from the email headers")
    content: EmailContent = Field(..., description="Extracted email body content")
    attachments: Optional[List[Attachment]] = Field(default_factory=list, description="List of extracted attachments")
    thread: Optional[EmailThread] = Field(None, description="Email threading information")
    transaction: Optional[TransactionData] = Field(None, description="Extracted transaction or policy data")
    compliance: Optional[ComplianceData] = Field(None, description="Extracted compliance-related data")
    action_items: Optional[List[ActionItem]] = Field(default_factory=list, description="List of actionable items found in the email")

# Example usage:
if __name__ == "__main__":
    sample_email_data = {
        "metadata": {
            "sender": "broker@example.com",
            "recipients": ["client@example.com"],
            "cc": ["assistant@example.com"],
            "bcc": [],
            "timestamp": "2025-02-05T14:30:00Z",
            "subject": "Your Policy Update",
            "message_id": "<unique.message.id@example.com>"
        },
        "content": {
            "text": "Dear Client, please review your updated policy details.",
            "html": "<p>Dear Client, please review your <strong>updated policy details</strong>.</p>",
            "links": ["https://example.com/policy-update"],
            "signature": "Best regards,\nYour Broker"
        },
        "attachments": [
            {
                "filename": "policy.pdf",
                "filetype": "application/pdf",
                "filesize": 234567
            }
        ],
        "thread": {
            "in_reply_to": "<previous.message.id@example.com>",
            "references": ["<previous.message.id@example.com>"]
        },
        "transaction": {
            "policy_number": "POL123456",
            "claim_id": "CLM654321",
            "transaction_amount": 1500.00
        },
        "compliance": {
            "keywords": ["confidential", "non-disclosure"],
            "confidentiality": True
        },
        "action_items": [
            {
                "description": "Review the attached policy document",
                "deadline": "2025-02-10T00:00:00Z"
            }
        ]
    }

    # Validate and parse the sample data
    email_extract = EmailExtract(**sample_email_data)
    print(email_extract.json())
