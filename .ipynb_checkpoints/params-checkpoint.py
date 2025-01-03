import sys, os, time
# nersc, interactive or not
interactive = 'False'
runtime = '00:05:00'

# add beam at first?
beam = False

# use Gaussian ksz or not
use_ksz_g = True


# add cmb map or not
use_cmb = True
# Gaussian kSZ realizations
ksz_g_realizations = 40

# maps information, 'Colin' or 'websky', 'lt' or 'ri'
map_source = 'websky'
ksz_type = 'lt'
decmax = 45
width_deg = 30
px_arcmin = 1
path = '/global/cscratch1/sd/hongbo/ksz_lens/'
map_path = path + 'maps/' + map_source + '/'

# alms fits files
cmb_alms_file = map_path + 'alms/' + 'lensed_cmb_alms_7000.fits'
ksz_alms_file = map_path +  'alms/' + f'ksz_{ksz_type}_alms_7000.fits'
ksz_g_alms_files = map_path + 'alms/' + f'ksz_g_{ksz_type}_alms_7000.fits'

kap_cls_file = map_path + 'cls/' + f'kap_cls_7000.csv'
kap_alms_file = map_path + 'alms/' + 'kap_alms_7000.fits'

# ksz_cls
smooth_ksz_cls_file = map_path + 'cls/' + f'smooth_ksz_{ksz_type}_cls_7000.csv'
ksz_cls_file = map_path + 'cls/' + f'ksz_{ksz_type}_cls_7000.csv'

# cutouts number
cutouts = int(2 * decmax / width_deg * (360 / width_deg))
print('cutout_num:', cutouts)
# output data path
data_path = 'output/data' + str(cutouts) + '/'


# experiments
experiments = {
    'Planck_SMICA': {
        'nlev_t': 45,
        'beam_arcmin': 5
    },
    'CMB_S3': {
        'nlev_t': 7,
        'beam_arcmin': 1.4
    },
    'CMB_S4': {
        'nlev_t': 1,
        'beam_arcmin': 3
    }
}

moments = {'moments1':{'ellmin':30, 'ellmax':3000, 'delta_L':150},'moments2':{'ellmin':30, 'ellmax':4000, 'delta_L':200}}

# moments = {'moments1':{'ellmin':30, 'ellmax':5000, 'delta_L':150}}


# salloc -N 1 -p debug -t 30 -C $CRAY_CPU_TARGET
# srun -n 4 uname -n
