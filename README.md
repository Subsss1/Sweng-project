# Wireshark dissector that classifies network traffic as human or machine generated

> Software Engineering Project 2024 - Group 11
>
> Client: Pico

## Project description

The project aims to develop a Wireshark dissector capable of classifying network traffic as either human-generated or machine-generated.
This involves collecting a dataset of network traffic examples, extracting relevant features and training machine learning models.
The dissector will then utilise these models to classify captured packets or flows in real-time, displaying the results within Wireshark's interface.
The end goal is to enhance network analysis by distinguishing between human and automated traffic patterns.

## Project structure

- [./Research.md](./Research.md) - Research during project development
- [./dissector](./dissector) - Wireshark dissector
  - [/ismachine.lua](./dissector/ismachine.lua) - Wireshark dissector plugin
  - [/server](./dissector/server) - Model server with which the dissector communicates
- [./model](./model) - Code and data used for model training
  - [/dumps](./model/convert) - Model dumps
  - [/datasets](./model/datasets) - Datasets used for model training
  - [/captures](./model/captures) - Traffic captures and corresponding labels
  - [/convert](./model/convert) - Scripts for labeling and converting traffic captures to datasets
- [./draft](./draft) - Drafts accumulated during the project development

<!-- !TODO -->
<!-- - [./Setup.md](./Setup.md) - Project setup guide -->

## Members

- Colm Buttimer
- Fifi Onafuwa
- Rhys Mac Giollabhuidhe
- Xingqiao Xu
- Yuheng Ye
- Rosemary Doyle
- Daniel Sorensen
- Alexander Judge
- Jesse Chambers
- Eoin Bande
- Andrii Yupyk
