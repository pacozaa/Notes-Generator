# Sticky Notes Synthetic Data Pipeline

## Set up the Conda environment

To set up the conda environment, run the following command.

```bash
conda create --name sticky-notes-synthetic-data python=3.10
```

To activate the environment, run the following command.

```bash
conda activate sticky-notes-synthetic-data
```

Then, install the required packages by running the following command.

```bash
pip install -e .
```

## Check if your environment is set up correctly

```bash
python -m chat.chat
```

or

```bash
chat "Hi"
```

For more information check out [pyproject.toml](pyproject.toml) and [chat/chat.py](chat/chat.py).

## Company Folder

The [company](company) folder contains the code to generate synthetic data for company sticky notes.

This is a synthetic data generator for company sticky notes. Diversify by using modified PersonaHub Dataset(https://huggingface.co/datasets/proj-persona/PersonaHub).

The way we modified is to mixing 3 personas randomly and filter only the word "business" to create a list of participants in the meeting then generate the sticky notes for the meeting.

Modified PersonaHub Dataset: https://huggingface.co/datasets/pacozaa/TeamPersonaHub_Business_StickyNotes_Batch_2

## Generate Synthetic Data

Run the following command to generate the synthetic data.

```bash
python company/sticky_notes_from_personas.py
```

or check out the file

[company/sticky_notes_from_personas.py](company/sticky_notes_from_personas.py)

## Mixer Folder

`mixer` is a folder that contains the code to mix word/sentence from different random datasets the list is [here](mixer/dataset_list.py).

To run the mixer, you can use the following command.

```bash
python mixer/mixer.py
```

## Generate Email/Conversation

```bash
# Email
generate_email
# Conversation
generate_conversation
```

## Load Email/Conversation

```bash
# Email
load_email
# Conversation
load_conversation
```

## Troubleshooting

1. Python package not found [chatgpt Q&A](https://chatgpt.com/share/67985d4f-bf80-8005-8b93-18317044d3d4)
