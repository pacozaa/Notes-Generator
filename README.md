# Sticky Notes Synthetic Data Pipeline

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
