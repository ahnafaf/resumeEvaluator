# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:50:01 2023

@author: ahnaf
"""
import PyPDF2
import docx

## Word Processing 

def docuReader(filename):
        doc = docx.Document(filename)  # Creating word reader object.
        data = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            data = '\n'.join(fullText)
        return data


def pdfReader(filename):
    fileData = ''
    reader = PyPDF2.PdfReader(filename)
    # print the text of the first page
    for i in reader.pages:
        stringText = i.extract_text()
        fileData += stringText
    return fileData


def checkerfunc(filename):
    if '.pdf' in filename:
        return pdfReader(filename)
    else:
        return docuReader(filename)
