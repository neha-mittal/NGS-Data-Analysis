FROM continuumio/miniconda3:4.8.2
COPY environment.yml .
RUN conda env create -f environment.yml
RUN useradd --shell /bin/bash my_user
USER my_user



WORKDIR /app
COPY . /app
CMD ["python", "python_file.py"]