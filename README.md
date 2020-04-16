# CS886-Project
Two Stage Multi-Document Summarization


#### Dependencies
- pytorch
- py-rouge

#### Download base model from link below (from nlpyang/PreSumm)
https://drive.google.com/file/d/1-IKVCtc4Q-BdZpjXc4s70_fRsWnjtYLr/view


#### Download Dataset from link below (from Alex-Fabbri/Multi-News)
https://drive.google.com/drive/folders/1qqSnxiaNVEctgiz2g-Wd3a9kwWuwMA07

#### Steps
- Install the necessary libraries based on GPU
- Download the models and data files and place them in their respective folders
- Execute the src/run_background.sh on a VM to trigger the experiment. Will need to update the data and model locations as necessary. This might needs some modification based on which stage is being executed.
- Execute the src/run_rouge.sh to run rouge scores
