**Individual equations**

1. Model way-level crashes

$CC_{cmow} =  e^{Ɑ_{movf}} * L_{w} * (EV_{cmw})^{0.4}$

Input: bicycle volume class = medium, pedestrian volume class = medium, bicycle functional class = minor road, pedestrian functional class = minor road, bicycle exposure = 50, pedestrian exposure = 100, length = 528 feet

Output (clean this up later):

|       | crash | injury | death |
|------------|-------|--------|-------|
| bicycle    | 0.006479752972821321 | 0.006399938546174876  | 0.0000798105472792838 |
| pedestrian | 0.0005025612581982916 | 0.00046553139561149337  | 0.00003702989425876207 |
| combined   | 0.0024379007085415555 | 0.0023318741573381987  | 0.00007344270530744104 |

2. Model intersection-level crashes

$CC_{cmoi} =  e^{Ɑ_{movf}} * (EV_{cmi})^{0.4}$

Input: bicycle volume class = medium, pedestrian volume class = medium, bicycle functional class = minor road, pedestrian functional class = minor road, bicycle exposure = 50, pedestrian exposure = 100

Output (clean this up later):

|       | crash | injury | death |
|------------|-------|--------|-------|
| bicycle    | 0.23665525955763556 | 0.2331519719675065 | 0.0035033178659148456 |
| pedestrian | 0.11882957851970188 | 0.11406042517643525 | 0.004769203707708837 |
| combined   | 0.22654948471430836 | 0.22030752178996574 | 0.005522112004484099 |

3. Total existing crashes - a mix of intersections and ways with different volumes and volume/functional classes (wait, what is the volume/functional class for combined mode? I get how it is calculated, but how do you assign it to a given node/way? need to figure that out before adding combined mode to this)

Input:
intersection 1: {pedestrian exposure = 600, bicycle exposure = 100, bicycle volume class = medium, pedestrian volume class = medium, bicycle functional class = minor road, pedestrian functional class = minor road}
intersection 2: {pedestrian exposure = 1000, bicycle exposure = 50, bicycle volume class = medium, pedestrian volume class = high, bicycle functional class = major road, pedestrian functional class = major road}

way 1: {pedestrian exposure = 100, bicycle exposure = 50, bicycle volume class = low, pedestrian volume class = low, bicycle functional class = minor road, pedestrian functional class = minor road, length = 528 feet}
way 2: {pedestrian exposure = 600, bicycle exposure = 200, bicycle volume class = medium, pedestrian volume class = medium, bicycle functional class = major road, pedestrian functional class = major road, length = 1056 feet}
way 3: {pedestrian exposure = 200, bicycle exposure = 100, bicycle volume class = medium, pedestrian volume class = medium, bicycle functional class = minor road, pedestrian functional class = minor road, length = 264 feet}

a) Model only total crashes

Output:
|       | crash | injury | death |
|------------|-------|--------|-------|
| bicycle    | 0.5675192248517249 | 0.558079161544122 | 0.00944012723993069 |
| pedestrian | 0.5335986390914865 | 0.5135308344530437  | 0.020067893569492255 |
| combined   | xxx | xxx  | xxx |

b) Split user and model total crashes

Input: model crashes same as above, user inputted crashes:

|       | bicycle | pedestrian |
|------------|-------|--------|
| crash   | 3 intersections,  2 roadway | 6 intersections, 4 roadway|
| injury | 2 intersections, 2 roadway | 5 intersections, 4 roadway  |
| death   | 1 intersections, 0 roadway | 1 intersections, 0 roadway  |
| years   | 3 years, 3 years | 3 years, 3 years |

Output:
|       | crash | injury | death |
|------------|-------|--------|-------|
| bicycle    | 1.2270076899406899 | 1.0232316646176487 | 0.20377605089597225 |
| pedestrian | 2.2134394556365944 | 2.0054123337812175 | 0.2080271574277969 |
| combined   | xxx | xxx  | xxx |

5. New Crashes (should I use real infrastructure types from the table or just put random numbers for the % crash decrease and % travel increase? Should I separate this by mode?)

$NC_{cmojk}=EC_{cmoj} * (1 + \sum_{i}\sum_{F}E_{ik} * \frac{Ni}{L} * I_{F})^{p}*CRF_{mojk}$

  a) length-based segment improvement

        Input: total existing crashes = 10, crash reduction factor = 50%, travel increase factor (Eik) = 25%, infrastructure length = 2640 feet, project length = 5280 feet, infrastructure type = new

        Output: 5.241203390786843

  b) count-based segment improvement

        Input: total existing crashes = 10, crash reduction factor = 50%, travel increase factor (Eik) = 25%, infrastructure count = 10, project length = 5280 feet, infrastructure type = new

        Output: 5.093384799130433

 c) count-based intersection improvement

        Input: total existing crashes = 10, crash reduction factor = 50%, travel increase factor (Eik) = 25%, infrastructure count = 10, project # of intersections = 20, infrastructure type = new

        Output (same as the first case): 5.241203390786843

d) combination

        Input: total existing crashes = 10, project length = 5280 feet, project # of intersections = 20
infrastructure 1: {travel increase factor (Eik) = 25%, crash reduction factor = 20%, infrastructure length = 2640 feet, infrastructure type = new}
infrastructure 2: {travel increase factor (Eik) = 15%, crash reduction factor = 10%, infrastructure length = 3696 feet, infrastructure type = new}
infrastructure 3: {travel increase factor (Eik) = 30%, crash reduction factor = 50%, infrastructure count = 15 (on segment), infrastructure type = new}
infrastructure 4: {travel increase factor (Eik) = 50%, crash reduction factor = 50%, infrastructure count = 15 (on intersection), infrastructure type = new}

        Output: 0.061680522832233284 crashes

6. Existing (weighted) miles traveled

a) Bike

Input: set of ways with length and bicycle demand
way 1: {bicycle demand = 50, length = 528 feet}
way 2: {bicycle demand = 75, length = 1056 feet}
way 3: {bicycle demand = 25, length = 264 feet}

Output: 170.0569558270192 miles

b) Walk

Input: set of intersections with adjacent ways length and pedestrian demand
intersection 1: {pedestrian demand = 200, adjacent selected ways lengths = 528 feet, 1056 feet}
intersection 2: {pedestrian demand = 400, adjacent selected ways lengths = 528 feet, 264 feet}
Project length: 1848 feet

Output: 216.78688524590174 miles

7. New miles traveled (oh, should this also have variations of different modes?)

$PT_{cmk}=WET_{cm} + \sum_{i}\sum_{F}E_{ik} * \frac{Ni}{L} * I_{F}$

  a) length-based segment improvement

        Input: existing miles traveled = 200 miles, project length = 5280 feet, travel increase factor (Eik) = 25%, infrastructure length = 2640 feet, infrastructure type = new

        Output: 225 miles

  b) count-based segment improvement

        Input: existing miles traveled = 200 miles, project length = 5280 feet, travel increase factor (Eik) = 25%, infrastructure count = 10, infrastructure type = new

        Output: 209.46969696969697 miles

  c) count-based intersection improvement

        Input: existing miles traveled = 200 miles, project # of intersections = 20, travel increase factor (Eik) = 25%, infrastructure count = 10, infrastructure type = new

        Output: 225 miles (same as part a)

  d) combination

        Input: existing miles traveled = 200 miles, project length = 5280 feet, project # of intersections = 20
infrastructure 1: {travel increase factor (Eik) = 25%, infrastructure length = 2640 feet, infrastructure type = new}
infrastructure 2: {travel increase factor (Eik) = 15%, infrastructure length = 3696 feet, infrastructure type = new}
infrastructure 3: {travel increase factor (Eik) = 30%, infrastructure count = 15 (on segment), infrastructure type = new}
infrastructure 4: {travel increase factor (Eik) = 50%, infrastructure count = 15 (on intersection), infrastructure type = new}

        Output: 338.04545454545456 s
