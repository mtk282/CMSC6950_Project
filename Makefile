default: report.pdf
.PHONY : default

report.pdf: report.tex total_argo.png argo_trajectory.png refs.bib
	latexmk -pdf

total_argo.png: plot_argo_byyear.py total_argo_2001.csv total_argo_2002.csv total_argo_2003.csv total_argo_2004.csv total_argo_2005.csv total_argo_2006.csv
	python3 plot_argo_byyear.py

argo_trajectory.png: plot_argo_trajectory.py argo_6902696.csv argo_6902754.csv
	python3 plot_argo_trajectory.py

argo_6902696.csv: argo_floats_sortdata.py argopy_task2.csv
	python3 argo_floats_sortdata.py

argo_6902754.csv: argo_floats_sortdata.py argopy_task2.csv
	python3 argo_floats_sortdata.py

total_argo_2001.csv: argo_region_sortdata.py argopy_task1.csv
	python3 argo_region_sortdata.py

total_argo_2002.csv: argo_region_sortdata.py argopy_task1.csv
	python3 argo_region_sortdata.py

total_argo_2003.csv: argo_region_sortdata.py argopy_task1.csv
	python3 argo_region_sortdata.py

total_argo_2004.csv: argo_region_sortdata.py argopy_task1.csv
	python3 argo_region_sortdata.py

total_argo_2005.csv: argo_region_sortdata.py argopy_task1.csv
	python3 argo_region_sortdata.py

total_argo_2006.csv: argo_region_sortdata.py argopy_task1.csv
	python3 argo_region_sortdata.py

argopy_task1.csv: data_argo_region.py
	python3 data_argo_region.py

argopy_task2.csv: data_argo_floats.py
	python3 data_argo_floats.py 

clean:
	rm *.csv
	rm *.png

.PHONY : clean

deepclean:
	rm *.pdf

.PHONY : deepclean


