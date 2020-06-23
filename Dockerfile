FROM python:3
WORKDIR /MathWorkSheetGenerator
COPY MainFile.py /
COPY WorSheetGenerator.py /
COPY AdditionWorkSheet.py /
COPY MultiplicationWorkSheet.py /
CMD [ "python", "./MainFile.py"]