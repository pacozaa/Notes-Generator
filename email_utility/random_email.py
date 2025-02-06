import random
import json
from datetime import datetime, timedelta
from faker import Faker
from pydantic import HttpUrl
from typing import Optional
from email_utility.email_extract_schema import EmailExtract

fake = Faker()

def random_email_data():
    metadata = {
        "sender": fake.email(),
        "recipients": [fake.email() for _ in range(random.randint(1, 3))],
        "cc": [fake.email() for _ in range(random.randint(0, 2))] if random.choice([True, False]) else [],
        "bcc": [fake.email() for _ in range(random.randint(0, 1))] if random.choice([True, False]) else [],
        "timestamp": fake.date_time_between(start_date="-30d", end_date="now").isoformat(),
        "subject": fake.sentence(),
        "message_id": fake.uuid4()
    }
    
    content = {
        "text": fake.paragraph() if random.choice([True, False]) else None,
        "html": f"<p>{fake.paragraph()}</p>" if random.choice([True, False]) else None,
        "links": [fake.url() for _ in range(random.randint(0, 3))] if random.choice([True, False]) else [],
        "signature": fake.name() if random.choice([True, False]) else None
    }
    
    attachments = [
        {"filename": fake.file_name(), "filetype": fake.mime_type(), "filesize": random.randint(1024, 500000)}
        for _ in range(random.randint(0, 2))
    ] if random.choice([True, False]) else []
    
    thread = {
        "in_reply_to": fake.uuid4() if random.choice([True, False]) else None,
        "references": [fake.uuid4() for _ in range(random.randint(0, 2))] if random.choice([True, False]) else []
    } if random.choice([True, False]) else None
    
    transaction = {
        "policy_number": fake.bothify(text="POL#######") if random.choice([True, False]) else None,
        "claim_id": fake.bothify(text="CLM######") if random.choice([True, False]) else None,
        "transaction_amount": round(random.uniform(100.0, 5000.0), 2) if random.choice([True, False]) else None
    } if random.choice([True, False]) else None
    
    compliance = {
        "keywords": [fake.word() for _ in range(random.randint(1, 3))] if random.choice([True, False]) else [],
        "confidentiality": random.choice([True, False])
    } if random.choice([True, False]) else None
    
    action_items = [
        {"description": fake.sentence(), "deadline": (datetime.now() + timedelta(days=random.randint(1, 14))).isoformat()}
        for _ in range(random.randint(0, 2))
    ] if random.choice([True, False]) else []
    
    email_data = {
        "metadata": metadata,
        "content": content,
        "attachments": attachments,
        "thread": thread,
        "transaction": transaction,
        "compliance": compliance,
        "action_items": action_items
    }
    
    return EmailExtract(**email_data)

if __name__ == "__main__":
    random_email = random_email_data()
    print(random_email.json())
