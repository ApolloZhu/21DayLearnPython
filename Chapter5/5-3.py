﻿import doctest

html = """
<h3>Contact Us</h3>
<p>Name: Mr.Wang</p>
<p>TEl: 021-87017800</p>
<div>
	<ul>
		<li><a class="nav-first" href="/">Home</a></li>
		<li><a href="/lista.php">Item1</a></li>
		<li><a href="/listb.php">Item2</a></li>
		<li><a href="/listc.php">Item3</a></li>
		<li><a href="/order/setorder.php">Order!</a></li>
		<li><a href="/about.php">About us</a></li>
	</ul>
</div>
"""

def getURL(html):
	"""
	>>> getURL(html)
	['/', '/lista.php', '/listb.php', '/listc.php', '/order/setorder.php', '/about.php']
	"""
	return list(
		map(
			lambda s: s[:s.find('"')], 
			list(
				filter(
					lambda s: not s == '', 
					html[html.find('href="'):].split('href="')
				)
			)
		)
	)

doctest.testmod()
