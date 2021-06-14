default: total_argo.png argo_trajectory.png report.pdf
.PHONY : default

report.pdf: report.tex total_argo.png argo_trajectory.png
	latexmk -pdf

total_argo.png: plot_total_argo.py argopy_task1.csv
	python3 plot_total_argo.py

argo_trajectory.png: plot_argo_float.py argopy_task2.csv
	python3 plot_argo_float.py

argopy_task1.csv: total_argo.py
	python3 total_argo.py

argopy_task2.csv: argo_float.py
	python3 argo_float.py 

clean:
	rm *.csv

.PHONY : clean

clean:
	rm *.png

.PHONY :clean

