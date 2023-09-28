from num2tib.core import convert

def test_convert():
    #test int
    assert convert(3,False) == 'གསུམ་'
    assert convert(1959,False) == 'གཅིག་སྟོང་དགུ་བརྒྱ་ལྔ་བཅུ་ང་དགུ་'
    assert convert(6000000,False) == 'ས་ཡ་དྲུག་'
    assert convert(608430,False)== 'འབུམ་དྲུག་དང་བརྒྱད་སྟོང་བཞི་བརྒྱ་སུམ་ཅུ་'
    

    #test float
    assert convert(3.14,False) == 'གསུམ་ཚེག་བཅུ་བཞི་'
    assert convert(3.01,False) == 'གསུམ་ཚེག་ཀླད་ཀོར་གཅིག་'
  
    #test str
    assert convert('1959',False) == 'གཅིག་སྟོང་དགུ་བརྒྱ་ལྔ་བཅུ་ང་དགུ་'
    assert convert('3.14',False) == 'གསུམ་ཚེག་བཅུ་བཞི་'
