FROM python:3
ADD MainFile.py /
ADD WorSheetGenerator.py /
ADD AdditionWorkSheet.py /
ADD MultiplicationWorkSheet.py /
CMD [ "python", "./MainFile.py"]
