def house_for_rent(bedrooms,walk_main,house_type,rent_yen):
    return {'bedrooms':bedrooms,'walk_main':walk_main,'house_type':house_type,'rent_yen':rent_yen}
house_for_rent(2,15,'アパート',50)


house_for_rent(2,'マンション',2,100)

house_for_rent(rent_yen=100,walk_main=2,bedrooms=2,house_type='マンション')

house_for_rent()

def hohouse_for_rent(bedrooms=2,walk_main=6,house_type='アパート',rent_yen=50):
    return {'bedrooms':bedrooms,'walk_main':walk_main,'house_type':house_type,'rent_yen':rent_yen}