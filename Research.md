# Documentation of Research Done Over the Course of the Project
Jesse Chambers
________________________________________________________________________________________________________________________________
One of our biggest problems with the project was trying to find a ready-made dataset to train our model on. To train our model we needed a PCAP file with enough data to make sure the model could differentiate between human and bot traffic with a sufficient level of accuracy. The idea seemed simple, search online for bot v human traffic files. An interesting source of PCAP files I found were ones artificially made to facilitate cyber security competitions. The files would contain examples of different types of bot attacks for the competitors to showcase their cyber defence skills. One of these I investigated was from the National CyberWatch Mid-Atlantic Collegiate Cyber Defense Competition (MACCDC), their domain being maccdc.org. 

Here are a couple examples of datasets researched.

https://share.netresec.com/s/wC4mqF2HNso4Ten

https://www.unb.ca/cic/datasets/ids-2017.html

The availability of appropriate datasets hindered our project in the beginning where I was mainly focused on their discovery and research. For example, the second link contained heavily detailed PCAP and CSV files which showcased different attacks, DDoS, injections etc., but the packets were only labelled as benign and malicious, not explicitly differentiating between human and bot.

For our demo we were not ready to use a large dataset and ended up using a small self-generated PCAP file instead.
________________________________________________________________________________________________________________________________
