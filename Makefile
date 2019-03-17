.DEFAULT_GOAL=quick

.PHONY: all quick

quick:

	python setup.py build_ext --inplace
	rm *.so
	rm -r build/*
	mv frccontrol/*.cpp ../src/frccontrol
	mv frccontrol/*.h ../include/frccontrol

all:

	python setup.py build_ext --inplace --force
	rm *.so
	rm -r build/*
	mv frccontrol/*.cpp ../src/frccontrol
	mv frccontrol/*.h ../include/frccontrol
