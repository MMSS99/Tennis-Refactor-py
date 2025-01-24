Refactoring exercise based on [Emily Banche's Tennis Refactoring Kata](https://github.com/emilybache/Tennis-Refactoring-Kata)
&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;    <sub>(Tennis1, 3 and tests, Python's version)</sub> 
## Refactoring commits
Instead of displaying each commit and changes in the README, each commit has a description in which the precise changes that have ocurred are briefly explained. The scope is described by conventional commits and the branch where it was originaly commited to. 

I've deemed as useless the effort that would be required to refactor Tennis2 and Tennis4 to 7 given their length or data structure used. 

I have used Pytest as the testing suite, so `tennis_unittest.py` only responsibility is to be imported by `tennis_test.py`. **It has not been refactored.**