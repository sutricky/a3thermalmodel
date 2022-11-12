# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi

RAWS := $(shell ls in/raw_*.csv)
DATES := $(patsubst in/raw_%.csv,%,$(RAWS))
BASES := $(patsubst in/raw_%.csv,out/base_%.csv,$(RAWS))
SOLARS := $(patsubst in/raw_%.csv,out/solar_%.csv,$(RAWS))
VFS := $(patsubst in/raw_%.csv,out/vf_%.csv,$(RAWS))
ALBEDOS := $(patsubst in/raw_%.csv,out/albedo_%.csv,$(RAWS))
EARTHS := $(patsubst in/raw_%.csv,out/earth_%.csv,$(RAWS))
DATASETS := $(patsubst in/raw_%.csv,out/dataset_%.csv,$(RAWS))
NODE_PREFIX := $(addprefix out/n, $(shell seq 1 7))
NODE_PATTERN := $(addsuffix _%.csv,$(NODE_PREFIX))
NODES := $(foreach date,$(DATES),$(addsuffix _$(date).csv, $(NODE_PREFIX)))
PREDICTIONS := $(patsubst in/raw_%.csv,out/prediction_%.csv,$(RAWS))
FIGURES := $(patsubst in/raw_%.csv,fig/%.png,$(RAWS))
BASEFIGURES := $(patsubst in/raw_%.csv,fig/base_%.png,$(RAWS))
RAWFIGURES := $(patsubst in/raw_%.csv,fig/raw_%.png,$(RAWS))
SOLARFIGURES := $(patsubst in/raw_%.csv,fig/solar_%.png,$(RAWS))
EARTHFIGURES := $(patsubst in/raw_%.csv,fig/earth_%.png,$(RAWS))
ALBEDOFIGURES := $(patsubst in/raw_%.csv,fig/albedo_%.png,$(RAWS))
ERRORFIGURES := $(patsubst in/raw_%.csv,fig/error_%.png,$(RAWS))
PAPERS := $(patsubst in/raw_%.csv,fig/paper_%.png,$(RAWS))
STATS := $(patsubst in/raw_%.csv,out/stat_%.txt,$(RAWS))
GRAPH_SOURCES := $(shell ls src/graph_*.py)
GRAPHS := $(patsubst src/graph_%.py,fig/graph_%.png,$(GRAPH_SOURCES))

include config.mk

.PHONY: all setup req clean-stat clean-fig clean-pred clean-graph

all: clean solar albedo earth dataset node prediction stat figure paper graph rawfig basefig solarfig earthfig albfig errorfig

clean:
	mkdir -p out fig
	rm -f out/* fig/*

clean-stat:
	rm -f out/stat*

clean-fig:
	rm -f fig/*.png

clean-pred:
	rm -f out/prediction*

clean-graph:
	rm -f fig/graph_*

base: $(BASES)

out/base_%.csv: in/raw_%.csv 
	pipenv run python3 src/calc_base.py $< $@

solar: $(SOLARS)

out/solar_%.csv: out/base_%.csv
	pipenv run python3 src/calc_solar.py $< $(CSSLIMIT) $@

vf: $(VFS)

out/vf_%.csv: in/tle_%.txt out/base_%.csv
	pipenv run python3 src/calc_vf.py $^ $(REARTH) $@

albedo: $(ALBEDOS)

out/albedo_%.csv: in/tle_%.txt out/base_%.csv out/vf_%.csv out/solar_%.csv
	pipenv run python3 src/calc_albedo.py $^ $@

earth: $(EARTHS)

out/earth_%.csv: out/base_%.csv out/vf_%.csv
	pipenv run python3 src/calc_earth.py $^ $@

dataset: $(DATASETS)

out/dataset_%.csv: out/base_%.csv out/solar_%.csv out/albedo_%.csv out/earth_%.csv
	pipenv run python3 src/create_dataset.py $^ $@

node: $(NODES)

$(NODE_PATTERN): out/dataset_%.csv
	pipenv run python3 src/create_nodeset.py $< $*

prediction: $(PREDICTIONS)

out/prediction_%.csv: out/dataset_%.csv $(NODE_PATTERN)
	pipenv run python3 src/create_predictions.py $^ $(RATIO) $(SEED) $@

stat: $(STATS)

out/stat_%.txt: out/prediction_%.csv
	pipenv run python3 src/create_stats.py $< $@

figure: $(FIGURES)

fig/%.png: out/prediction_%.csv
	pipenv run python3 src/create_figures.py $< $*

paper: $(PAPERS)

fig/paper_%.png: out/prediction_%.csv
	pipenv run python3 src/create_paperfigures.py $< $*

graph: $(GRAPHS)

fig/graph_%.png: src/graph_%.py
	pipenv run python3 $<

rawfig: $(RAWFIGURES)

fig/raw_%.png: out/base_%.csv
	pipenv run python3 src/create_rawfigures.py $< $*

basefig: $(BASEFIGURES)

fig/base_%.png: out/base_%.csv
	pipenv run python3 src/create_basefigures.py $< $*

solfig: $(SOLARFIGURES)

fig/solar_%.png: out/base_%.csv out/solar_%.csv
	pipenv run python3 src/create_solarfigures.py $^ $*

earthfig: $(EARTHFIGURES)

fig/earth_%.png: out/base_%.csv out/earth_%.csv
	pipenv run python3 src/create_earthfigures.py $^ $*

albfig: $(ALBEDOFIGURES)

fig/albedo_%.png: out/base_%.csv out/albedo_%.csv
	pipenv run python3 src/create_albedofigures.py $^ $*

solarfig: $(SOLARFIGURES)

fig/solar_%.png: out/base_%.csv out/earth_%.csv
	pipenv run python3 src/create_solarfigures.py $^ $*

errorfig: $(ERRORFIGURES)

fig/error_%.png: out/prediction_%.csv
	pipenv run python3 src/create_errorfigures.py $< $*

icares: out/prediction_2018-05-19.csv out/prediction_2018-05-20.csv
	pipenv run python3 src/create_icares.py $^

setup: Pipfile Pipfile.lock
	pipenv install

req: Pipfile Pipfile.lock
	pipenv requirements > requirements.txt
