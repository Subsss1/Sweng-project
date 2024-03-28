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
Rosemary Doyle
_________________________________________________________________________________________________________________________________

In the begining of the project, I was assigned to the dissector team. Researching the dissector and it's implementation as well as gaining a good understanding of Lua was a large portion of the first week of work. Wireshark and Lua's own resources provided guidance in how to go about implementing the disector. 

https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html
https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm_modules.html
https://www.lua.org/pil/contents.html

Finding an appropriate dataset was the biggest challenge we had to overcome in this project, I searched through many databases for appropriate dataset, but the options were extremely limited and often times didn't contain the information we needed and/or contained much information that was irrelevant. The University of New Brunswick had some very promising datasets from the Canadian Institute for Cybersecurity, but they were too specified for our needs, i.e. datasets would contain only a specific type of machine-generated traffic or would focus on a single issue.

https://www.unb.ca/cic/datasets/index.html

KDD Cup 1999 Data also seemed promising, but as the title suggests it is rather outdated and introduces the fear that it may be inaccurate for todays standards and therefore essentially useless.

http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

There were many other databases of datasets searched, all of which had individual reasons for not being used, and many of which I could not confirm to be reliable sources as they had no connections (that I could find) to reputable sources.

I then worked for a short period of time on the influx database, Influx University provided a short (roughly 6-9hr) course on getting started with InfluxDB which was extremely useful.

https://university.influxdata.com/courses/influxdbu-essentials-iox/
_________________________________________________________________________________________________________________________________
Alexander Judge
_________________________________________________________________________________________________________________________________
I was assigned to the model team for the project. I had no experience with python nor machiene learning so because of that I had to do a good amount of research before hand. Our group looked into binary classification and sklearn for our model. 

https://scikit-learn.org/stable/
https://visualstudiomagazine.com/articles/2023/02/21/scikit-decision-tree.aspx
https://www.learndatasci.com/glossary/binary-classification/
https://www.youtube.com/watch?v=Rg71lBtEuTc

These are the links that helped me get started with the model. 

After getting progress done on the model, I switched over to docker and github packaging.

I used these videos to get started.

https://www.youtube.com/watch?v=gqseP_wTZsk&t=0s
https://www.youtube.com/watch?v=gcacQ29AjOo&t=0s
https://www.youtube.com/watch?v=SnSH8Ht3MIc&t=0s

These helped me get a dockerfile generated and github package, I also used github actions to make a pre release. 





