"""
Tipe Data Dictionary sekedar menghubungkan Key dan Value
KVP = Key Value Pair
Dictionary = Kamus
"""

kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print( f'\nkamus_ind_eng' )
print( kamus_ind_eng['ayah'] )
print( kamus_ind_eng['istri'] )
print( kamus_ind_eng['ibu'] )

print( f'\nData ini dikirimkan oleh server Gojek untuk memberikan info driver di sekitar pemakai aplikasi' )
data_dari_server_gojek = {
    'tanggal': ('2020-2-1'),
    'driver_list': [
        {'nama': 'Kenar', 'jarak': 10},
        {'nama': 'Senja', 'jarak': 35},
        {'nama': 'Gantari', 'jarak': 250},
        {'nama': 'Rinjani', 'jarak': 115}]
}
print( data_dari_server_gojek )
print( f"\ndriver di sekitar sini {data_dari_server_gojek['driver_list']}" )
print( f"driver #1` {data_dari_server_gojek['driver_list'][0]}" )
print( f"driver #3` {data_dari_server_gojek['driver_list'][2]}" )
print( f"driver #2` {data_dari_server_gojek['driver_list'][1]}" )
print( f"driver #4` {data_dari_server_gojek['driver_list'][3]}" )

print(f"driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")