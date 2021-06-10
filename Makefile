default: total_argo_float.pdf
.PHONY : default

argopy_task1.csv: argopy


total_argo_float.pdf: total_argo_float.py argopy_task1.csv
	python3 total_argo_float.py

clean:
	rm *.csv

.PHONY : clean

