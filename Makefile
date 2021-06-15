default: report.pdf
.PHONY : default

report.pdf: report.tex total_argo.png argo_trajectory.png refs.bib
	latexmk -pdf

total_argo.png: plot_total_argo.py total_argo_2001.csv total_argo_2002.csv total_argo_2003.csv total_argo_2004.csv total_argo_2005.csv total_argo_2006.csv
	python3 plot_total_argo.py

argo_trajectory.png: plot_argo_float.py argo_6902696.csv argo_6902754.csv
	python3 plot_argo_float.py

argo_6902696.csv: argo_float_sort.py argopy_task2.csv
	python3 argo_float_sort.py

argo_6902754.csv: argo_float_sort.py argopy_task2.csv
	python3 argo_float_sort.py

total_argo_2001.csv: total_argo_byyear.py argopy_task1.csv
	python3 total_argo_byyear.py

total_argo_2002.csv: total_argo_byyear.py argopy_task1.csv
	python3 total_argo_byyear.py

total_argo_2003.csv: total_argo_byyear.py argopy_task1.csv
	python3 total_argo_byyear.py

total_argo_2004.csv: total_argo_byyear.py argopy_task1.csv
	python3 total_argo_byyear.py

total_argo_2005.csv: total_argo_byyear.py argopy_task1.csv
	python3 total_argo_byyear.py

total_argo_2006.csv: total_argo_byyear.py argopy_task1.csv
	python3 total_argo_byyear.py

argopy_task1.csv: total_argo.py
	python3 total_argo.py

argopy_task2.csv: argo_float.py
	python3 argo_float.py 

clean:
	rm *.csv
	rm *.png

.PHONY : clean

deepclean:
	rm *.pdf

.PHONY : deepclean


