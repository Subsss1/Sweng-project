# make capture2dataset capture=capture.pcapng labels=labels.csv output=output.csv
capture2csv:
	python3 ./capture2dataset.py $(capture) $(labels) $(output)

# make dissections2labels dissections=dissections.csv output=output.csv
dissections2labels:
	python3 ./dissections2labels.py $(dissections) $(output)
