File: machine\calc_correlation.py
	  File "calc_correlation.py", line 40
	    print "Usage: python calc_correlation.py <data file.py>"

	  File "calc_correlation.py", line 46
	    print movies_list

	  File "calc_correlation.py", line 52
	    print correlated_dict

Cause: Python 2 vs 3 problem / Missing parentheses in call to 'print'


File: machine\ml_main.py
	  File "C:\Devel\PyEng\machine\ml_main.py", line 41
	    print "total_my_votes = ", total_my_votes

	  File "C:\Devel\PyEng\machine\ml_main.py", line 47
	    print recommended_movies

	  File "C:\Devel\PyEng\machine\ml_main.py", line 51
	    print "Strongly recommended for you: ", movie_key

	  File "C:\Devel\PyEng\machine\ml_main.py", line 53
	    print "Recommended for you: ", movie_key

	  File "C:\Devel\PyEng\machine\ml_main.py", line 55
	    print "Not recommended: ", movie_key

Cause: Python 2 vs 3 problem / Missing parentheses in call to 'print'


rpi\webapp.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\rpi\webapp.py", line 3, in <module>
	    from flask import *
	ModuleNotFoundError: No module named 'flask'

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)

	Traceback (most recent call last):
	  ...
	  File "C:\Devel\PyEng\rpi\webapp.py", line 19, in home
	    msg = msg.split("\n")

Cause: Python 2 vs 3 problem / Bytes vs Str
Fix: msg = msg.split(b"\n").

rpi\webapp_bootstrap.py
	File: rpi\webapp_bootstrap.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\rpi\webapp_bootstrap.py", line 3, in <module>
	    from flask import *
	ModuleNotFoundError: No module named 'flask'

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)

	Traceback (most recent call last):
	 ...
	 File "C:\Devel\PyEng\rpi\webapp_bootstrap.py", line 19, in home
	    msg = msg.split("\n")

Cause: Python 2 vs 3 problem / Bytes vs Str
Fix: msg = msg.split(b"\n").


audio/get_freq.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\audio\get_freq.py", line 6, in <module>
	    import numpy as np

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)


audio/noisy.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\audio\noisy.py", line 6, in <module>
	    import numpy as np

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)

audio/noisy.py produced warning:
	...\site-packages\numpy\core\numeric.py:531: ComplexWarning: Casting complex values to real discards the imaginary part
	  return array(a, dtype, copy=False, order=order)


Plotting\data_plot.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\Plotting\data_plot.py", line 6, in <module>
	    import numpy as np

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)


Plotting\graph_wave.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\Plotting\graph_wave.py", line 6, in <module>
	    import numpy as np

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)


Plotting\list_comp.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\Plotting\list_comp.py", line 6, in <module>
	    import numpy as np

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)


Pandas\obesity.py
	  File "C:\Devel\PyEng\Pandas\obesity.py", line 5
	    print  data.sheet_names

	  File "C:\Devel\PyEng\Pandas\obesity.py", line 28
	    print data_age

Cause: Python 2 vs 3 problem / Missing parentheses in call to 'print'


Pandas\pandas_movie.py
	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 19
	    print "Top rated movies (overall): \n" , movie_data.groupby('title').size().order(ascending=False)[:20]

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 20
	    print "\n"

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 21
	    print "\n"

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 34
	    print "Top ten movies for teens: \n", teens[:10]

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 35
	    print "\n"

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 36
	    print "Top ten movies for oldies: \n", oldies[:10]

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 37
	    print "\n"

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 38
	    print "\n"

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 49
	    print "Top rated movies by women \n", top_movies_women.head()

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 50
	    print "\n"

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 55
	    print "Difference by gender \n", ratings_by_gender.head()

	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 56
	    print "\n"

Cause: Python 2 vs 3 problem / Missing parentheses in call to 'print'

	Traceback (most recent call last):
	  File "C:\Devel\PyEng\Pandas\pandas_movie.py", line 12, in <module>
	    movies = pd.read_csv('movie_lens/u.item', sep='|', names=movie_columns, usecols=range(2))
	  ...
	UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 3: invalid continuation byte

Cause: Python 2 vs 3 problem / Python3 default encoding versus Python2 default
Fix: specify 'Latin_1' encoding during csv read as example:
	movies = pd.read_csv('movie_lens/u.item', sep='|', names=movie_columns, usecols=range(2), encoding='Latin_1')

Suggest: do same for all read_csv. Seems these files encoded using Latin1 (same as iso-8859-1). 
More on encodings: https://docs.python.org/3/library/codecs.html#standard-encodings

Pandas\pandas_movie.py produced some warnings:
	...Pandas\pandas_movie.py:47: FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)
	  top_movies_women = ratings_by_gender.sort_index(by='F', ascending=False)

	...Pandas\pandas_movie.py:62: FutureWarning: sort is deprecated, use sort_values(inplace=True) for INPLACE sorting
	  gender_diff.sort(ascending = False)


Multiprocessing\gen_rand.py
	  File "C:\Devel\PyEng\Multiprocessing\gen_rand.py", line 9
	    print "job done"

Cause: Python 2 vs 3 problem / Missing parentheses in call to 'print'


Image_Video\color_test.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\Image_Video\color_test.py", line 6, in <module>
	    from SimpleCV import *

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)

	Traceback (most recent call last):
	  File "C:\Devel\PyEng\Image_Video\color_test.py", line 6, in <module>
	    from SimpleCV import *
	  File "C:\Users\joskis\Envs\PyEng\lib\site-packages\SimpleCV\__init__.py", line 3, in <module>
	    from SimpleCV.base import *
	  File "C:\Users\joskis\Envs\PyEng\lib\site-packages\SimpleCV\base.py", line 139
	    print 'unit test'

Cause: SimpleCV does not support Python3
Fix: ether rewrite to use another library (OpenCV) or wait until SimpleCV supports Python3


Image_Video\color_train.py
Has python2 shebang, should be updated to python3 shebang or removed.
Uses SimpleCV. SimpleCV does not support Python3
Fix: ether rewrite to use another library (OpenCV) or wait until SimpleCV supports Python3


Image_Video\count_cards.py
Traceback (most recent call last):
  File "C:\Devel\PyEng\Image_Video\count_cards.py", line 21, in <module>
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ValueError: too many values to unpack (expected 2)

Cause: OpenCV version issue. Using version 3.2. findContours returns 3 values:
	http://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html
Fix: im2, contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


Image_Video\face_detect.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\Image_Video\face_detect.py", line 7, in <module>
	    import cv2

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)


Image_Video\motion_detect.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\Image_Video\face_detect.py", line 7, in <module>
	    import cv2

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)


Image_Video\webcam_face_detect.py
	Traceback (most recent call last):
	  File "C:\Devel\PyEng\Image_Video\face_detect.py", line 7, in <module>
	    import cv2

Cause: Shebang on first line, uses python2
Should be: "#!/usr/bin/python3" or "#!/usr/bin/env python3" or removed if Windows + virtualenv is used (https://www.python.org/dev/peps/pep-0486/)


Multiprocessing\gen_rand.py
Multiprocessing\process.py
Multiprocessing\single.py
Multiprocessing\thread.py

Has python2 shebang, should be updated to python3 shebang or removed.


WordCount\count_lines_fixed.py
WordCount\count_words.py
WordCount\read_file.py
WordCount\word_count.py

Has python2 shebang, should be updated to python3 shebang or removed.

