# Annotator
A tool that allow you to quickly annotate your NER tags.
A detailed tutorial is also uploaded, see Annotator_Tutorial.mp4

## 1. Open gpt, and copy the following instructions for him:

```
Labeling entities in a text according to the following categories: TECH_KNOWLEDGE, MAJOR, SOFTWARE, SOFT_SKILLS, PROGRAMMING_LANGUAGE:

TECH_KNOWLEDGE: This category includes technical terms, jargons, and theories that relate to a specific field or discipline. Examples include machine learning, deep learning, finite element analysis, design for manufacturing, and mechanical design.
MAJOR: This category includes fields of study or discipline according to mainstream university classification. Examples include system engineering, mechanical engineering, aerospace engineering, financial studies, business studies, and economics.
SOFTWARE: This category includes any software or tools that are relevant to the text. Examples include SolidWorks, Fusion, Creo, Abaqus, Ansys, and Matlab.
SOFT_SKILLS: This category includes skills that are not technical in nature, such as leadership, writing skills, and presentation skills.
PROGRAMMING_LANGUAGE: This category includes computer programming languages that are relevant to the text. Examples include Java, C++, C, C#, Python, and R.

For each piece of text, do the following:

Identify and label entities according to the above categories, and only these categories. Other categories are strictly forbidden.
The labels should be separated by a "@@" symbol, no line break.
Each label should be followed by a sequence of entities after "&&".
The sequence of entities within each label should be separated by "%%".
The number of entities in each category is indeterminate.
There should be no repeated entities within each category.
The categories are mutually exclusive (i.e., an entity should only be included in one category).
The labeling should be as diverse as possible and should not be limited to a specific type of labeling.
The entities should be coherent and should all be nouns.
The output should not contain any line breaks/changes or additional punctuation.
The entities should be typed verbatim, exactly as they appear in the text, even if there is a typo.
If possible, whole phrases should be recognized as a single entity.
DO NOT include words that are not in the text. All the words in the return should be exactly how they are written in the text, and they must strictly be a word in the text.
Only consider the text provided in the current input. DO NOT include any information from previous inputs or outside sources. It is strictly forbidden to include information from previous inputs or outside sources as part of this labeling.
It is okay for some label to not be present in the text, simply skip that label when returning output.
If nothing falls under any category, return "!".
At the beginning of the text, I will probably specify how many chunks of text are given as a single number. Chunks are separated by a line gap. If not specified, I will default to one chunk at a time.
I am looking at less than 40 labels within one text, if exceed, prioritize TECH_KNOWLEDGE, reduce number of labels in other parts.

Example:

Input text: "I took Buisiness class before.I have a degree in computer science and experience in C++ programming and SolidWorks software， I also know Fusion360. Sometimes it is good to know Java."

Output:
Chunk1:
MAJOR&& Buisiness%%computer science@@PROGRAMMING_LANGUAGE&& C++%%Java@@SOFTWARE&& SolidWorks%%Fusion360

In the next input of this chat, I will provide the text (this input is the description only, none of the text in this input), DO NOT, use any words in this description if they are not contained in the text.

Respond "Sure" if you understand and are ready for the text input.
```

You should see GPT respond "sure".\
Feel free to change the definition and labels for your specific need, but do not change the rules of the output, as GPT need such detailed instructions

## 2.Copy the text you want to label into GPT, wait for its response

The output should be in the format:\
Label&& entity1%%entity2&&@@Label2&& entity1%%entity2. If it is not correct, tell GPT what is wrong and let it redo.\

## 3.Copy what gpt returns, and put it in a txt file. 

Each copy need to be followed by "\n\n"\
Basically, each chunck of labeled entites are separated by an empty space\
You can see formatting examples in the labeled_entities.txt file

## 4.Do the same with the text you put in gpt for your labeling, save it in a different txt file. You MUST follow the format:

Within each chunck of text, it should not contain any line changes. The program separate chunks by "\n\n".\
At the end of the text, you should add "\n\n" for the program to read properly.

## 5. Make sure your text and labels are one-to-one:

Text chunks and label chuncks should have the same number. Otherwise it won't work.\
If you have 100 chunks in the text, you should also have 100 chunks in the labeling.

## 6. Generate the .json, easy for you to create dataset.

Open the quick_annotator.exe or run the quick_annotator.py by double click. \
Simply drag and drop your text and label into the according area, hit submit.\
You will see a prompt asking you to specify where to save your .json file. Name it, and save.\
You should see the prompt "process completed successfully".
