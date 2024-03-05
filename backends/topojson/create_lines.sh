#!/bin/bash

radars=( ade adw bks cve cvw cly fhe fhw gbr han hok hkw inv jme kap ksr kod lyr pyk pgr rkn sas sto wal bpk dce dcn fir hal ker mcm san sps sye sys tig unw zho )

ade_beams=22
ade_gates=110

adw_beams=22
adw_gates=110

bks_beams=24
bks_gates=110

cve_beams=24
cve_gates=75

cvw_beams=24
cvw_gates=75

cly_beams=16
cly_gates=75

fhe_beams=22
fhe_gates=110

fhw_beams=22
fhw_gates=110

gbr_beams=16
gbr_gates=100

han_beams=16
han_gates=75

hok_beams=16
hok_gates=110

hkw_beams=16
hkw_gates=100

inv_beams=16
inv_gates=75

jme_beams=24
jme_gates=100

kap_beams=16
kap_gates=100

ksr_beams=16
ksr_gates=75

kod_beams=16
kod_gates=75

lyr_beams=16
lyr_gates=110

pyk_beams=16
pyk_gates=75

pgr_beams=16
pgr_gates=75

rkn_beams=16
rkn_gates=75

sas_beams=16
sas_gates=75

sto_beams=16
sto_gates=75

wal_beams=24
wal_gates=110

bpk_beams=22
bpk_gates=110

dce_beams=16
dce_gates=75

dcn_beams=16
dcn_gates=75

fir_beams=16
fir_gates=75

hal_beams=16
hal_gates=75

ker_beams=16
ker_gates=75

mcm_beams=16
mcm_gates=75

san_beams=16
san_gates=75

sps_beams=16
sps_gates=75

sye_beams=16
sye_gates=75

sys_beams=16
sys_gates=75

tig_beams=16
tig_gates=75

unw_beams=16
unw_gates=75

zho_beams=16
zho_gates=75

for rad in "${radars[@]}"
do
	python3 create_geojson_lines.py ${rad} $(eval "echo \$${rad}_beams") $(eval "echo \$${rad}_gates")
done

for rad in "${radars[@]}"
do
	geo2topo -q 1e4 topojsondata=${rad}geojson_lines.json > ${rad}topojsonlines.json 
done
