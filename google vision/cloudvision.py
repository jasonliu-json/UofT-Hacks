import io
import os
from languagedictionary import languages

# Environment variable set before anything happens instead of being set beforehand everytime in terminal
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="My First Project-1d639f1cdfdf.json"

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import translate

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'cat2.jpg') # <================================ PICTURE INPUT 

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

numofdescriptions = 0

for label in labels:
    theword = label.description
    numofdescriptions += 1
    if numofdescriptions == 1:
        break

for langcode, langinput in languages.items():    
    if langinput == 'Tajik': # <================= USER INPUT FOR LANGUAGE
        # The target language
        target = langcode

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = (theword)

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'{}'.format(text)) # <=============== THE OBJECT NAME IN ENGLISH
print(u'{}'.format(translation['translatedText'])) # <============ THE OBJECT NAME IN ANOTHER LANGUAGE
