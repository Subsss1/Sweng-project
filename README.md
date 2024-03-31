Software Engineering Project 2024
Group 11

Client: Pico

Project Description:
The project aims to develop a Wireshark dissector capable of classifying network traffic as either human-generated or machine-generated. 
This involves collecting a dataset of network traffic examples, extracting relevant features and training machine learning models. 
The dissector will then utilise these models to classify captured packets or flows in real-time, displaying the results within Wireshark's interface. 
The end goal is to enhance network analysis by distinguishing between human and automated traffic patterns.

Members:
Colm Buttimer,
Fifi Onafuwa,
Rhys Mac Giollabhuidhe,
Xingqiao Xu,
Yuheng Ye,
Rosemary Doyle,
Daniel Sorensen,
Alexander Judge,
Jesse Chambers,
Eoin Bande,
Andri Yupyk 

Method to use dissector:
1.Clone the library and select the latest master branch.
2.Open the ismachine.lua file in the dissector folder. (If you're using a mac, skip this step.)
Check whether the Windows path is the same as the plugin folder in the local wireshark installation directory. 
If inconsistent, change Windows path to the plugin folder in the local wireshark installation folder.
3.Copy ismachine.lua and inference.py and model.pkl in the model folder. (The connection of the model is not yet complete, but model.pkl will be needed in the future.)
Put them in the plugins folder under the wireshark installation directory.
4.Open an arbitrary.pcapng file and you should be able to find that the plugin is already running.
