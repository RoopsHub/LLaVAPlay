# LLaVAPlay
This app uses localized LLaVA LLM to provide textual interpretation of a image, also we compare AI generated images with prompt and compare it with the description generated from LLaVA LLM 
**Step1: Localize the LLM**
For this application we are using LLaVA LLM from LLaVA is an open-source chatbot trained by fine-tuning LLaMA/Vicuna on GPT-generated multimodal instruction-following data.
Instead of localizing the whole model (gguf) we used LLaMA file version of LLaVA ( https://huggingface.co/Mozilla/llava-v1.5-7b-llamafile )
**Step2: Execute the llamafile**
For executing the file use the command ./llava-v1.5-7b-llamafile in terminal window where the file is stored
Post execution llama.cpp page is opened in the browser in localhost port 8080
Where you can upload pictures directly and ask question
![image](https://github.com/user-attachments/assets/6e654eb2-7ff9-4caa-894b-11634a35ebe2)
**Step3: Build the application**
Next step is the creation of the application using python
Requirement.txt file lists the required libraries for exectuing this app
App output looks like below snippet
![image](https://github.com/user-attachments/assets/b5318133-4554-4396-b99b-5739e32ea03a)
