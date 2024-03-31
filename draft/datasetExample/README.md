# Notes

# USE human_update_EXAMPLE.csv and update_TEST.csv for model training 
(EXAMPLE SET)
1. Capture traffic in Wireshark, filter results by tcp || udp
2. Save as pcap, open file and export to CSV
3. open in excel, > data > filter > source > remove ipv6, save

In terminal /datasetExample

4. run python data_clean.py [.csv file]
5. run python add_label.py human update_EXAMPLE.csv labelled_EXAMPLE.csv

(TEST SET)
run capture again, repeat 1 - 4
then open in excel and add "Human" as last column header 