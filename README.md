# Identifying First-Person Narrative Voice
#### Video Demo:  <https://youtu.be/xkusl7jjG0w>
#### Description:
My project enables users to input a link or a txt file and then determines whether the text contained is written in first-person narrative voice or is epistolary.  A narrative written in first-person voice is generally told from a character's perspective, and an epistolary text is one written in letters.  The pronoun "I" appears quite frequently in such texts because a character who is involved in the narrative is also relating the narrative.  Since I am working with first-person and epistolary texts in my current project and I am interested in far more texts than I have time to read, I wanted to develop a tool that could quickly assess narrative voice.

The main program is fairly straightforward.  After the user inputs a valid website with text or plain text file, the program:

- extracts the text to memory
- counts and prints the total number of words in the text
- counts the total number of I's in the text
- calculates what I call the "I ratio" in the text
- predicts whether or not the text is a first-person narrative

The first few steps of the program - opening and extracting text and counting words - are not unusual.  It is where we get to the "I" counting that certain decisions had to be made.  I used regular expressions to find the number of I's in a given document:
```
matches = re.findall(r"\s[i](\s|')", text)
```
By writing the expression in this way, I have excluded all I's that appear directly after a quotation mark.  Since quoted statements beginning with I occur in both third and first-person narratives (since quotations are individual narratives), this prevents the "I count" for third-person narratives from getting artificially high.  This doesn't eliminate all I's from quoted language: just the ones closest to the quotation mark.

I then create a ratio of the number of I's that appear in the text to the total number of words.  I ran a number of tests on various types of novels and following those tests propose that if the ratio is greater than 0.024, the novel is probably first-person or epistolary.  If that ratio is less than 0.016, it is unlikely to be first-person or epistolary.  Everything in between was ambiguous, often depending on how experimental a text was or if it was a framed narrative (a first-person narrative in an outer frame with an inner narrative largely from the third-person point of view).

Besides the program and the README, there are a few other files.  The first is the requirements: the libraries required are sys, os.path, re, validator_collection, urllib.request and BeautifulSoup, with the latter two requiring a pip install.  There is the test_project program with three functions to be tested using pytest.  I have included a short test.txt file that served as the tester text file as I developed the program. Finally, the data.txt file contains the results for nearly 40 novels, mostly from the eighteenth century.  That data serves as the rationale behind the ratio cut-offs in the main program.

In general, the program was quite accurate at identifying first-person and epistolary voice, especially if the narrative was straightforward.  I hope to continue to use this and perhaps combine it with sentiment analysis in the future.