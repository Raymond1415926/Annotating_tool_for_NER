# Annotator
A tool that allow you to quickly annotate your NER tags.
A detailed tutorial is also uploaded, see Annotator_Tutorial.mp4

# 1. Open gpt, and copy the following instructions for him:

```
Labeling entities in a text according to the following categories: TECH_KNOWLEDGE, MAJOR, SOFTWARE, SOFT_SKILLS, PROGRAMMING_LANGUAGE:

TECH_KNOWLEDGE: This category includes technical terms, jargons, and theories that relate to a specific field or discipline. Examples include machine learning, deep learning, finite element analysis, design for manufacturing, and mechanical design.
MAJOR: This category includes fields of study or discipline according to mainstream university classification. Examples include system engineering, mechanical engineering, aerospace engineering, financial studies, business studies, and economics.
SOFTWARE: This category includes any software or tools that are relevant to the text. Examples include SolidWorks, Fusion, Creo, Abaqus, Ansys, and Matlab.
SOFT_SKILLS: This category includes skills that are not technical in nature, such as leadership, writing skills, and presentation skills.
PROGRAMMING_LANGUAGE: This category includes computer programming languages that are relevant to the text. Examples include Java, C++, C, C#, Python, and R.
For each piece of text, identify and label entities according to the above categories. The labels should be separated by a "#" symbol, and each label should be followed by a list of entities separated by a comma.

The number of entities in each category is indeterminate. There should be no repeated entities within each category, and the categories are mutually exclusive (i.e., an entity should only be included in one category).

The labeling should be as diverse as possible and should not be limited to a specific type of labeling. The entities should be coherent and should all be nouns.

The output should not contain any line breaks or additional punctuation.

The entities should be typed verbatim, exactly as they appear in the text, even if there is a typo. For example, if the text contains the word "engineing", the return should still be "engineing".

If possible, whole phrases should be recognized as a single entity. For example, "DDR PHY/Controller" should be recognized as a single entity, even though it contains multiple single-word keywords.

DO NOT include words that are not in the text. All the words in the return should be exactly how they are written in the text, and they must strictly be a word in the text.

Only consider the text provided in the current input. DO NOT include any information from previous inputs or outside sources.

It is okay for some label to not present in the text, simply skip that label when returning output

Here is an example of the desired output format, using the text "I have a degree in computer science and experience in C++ programming and SolidWorks software":

MAJOR: computer science#PROGRAMMING_LANGUAGE: C++#SOFTWARE: SolidWorks

In the next input of this chat, I will be providing the text (this input is the description only, none of the text in this input)
Again, you should only consider texts within the next input, nothing else, stricktly forbidden to include older inputs as part of this extraction.
Respond "Sure" if you understand and are ready for the text input.
```

You should see gpt respond "sure".
Feel free to change the definition of the labels, but do not change the rules of the output, as gpt need such detailed instructions

# 2.Copy the text you want to label into GPT, wait for its response

# 3.Copy what gpt returns, and put it in a txt file. Each copy need to be followed by "\n\n"
You can see formatting examples in the labeled_entities.txt file

# 4.Do the same with the text you put in gpt for your labeling, save it in a different txt file. You MUST follow the format:
In each chunck of text, you should get rid of all the "\n"
At the end of the text, you should add "\n\n"

# 5. Make sure your enteries in the text file is one-to-one matching with the enteries in the labeled entities file:
They should have same numbers of entieries, otherwise this won't work.

# 6. Open the quick_annotator.ext and drag and drop, hit submit, the program will return a .json file in the directory you specified.

