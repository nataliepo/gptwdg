<!DOCTYPE html> 
<html lang="en"> 

<head>
    <meta charset="utf-8"> 

        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
        <meta http-equiv="Content-Style-Type" content="text/css" /> 
        <meta http-equiv="Content-Script-Type" content="text/javascript" />

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

	    <script src="static/js/jquery-1.7.2.min.js"></script>  
        <script src="static/js/utilities.js?${random_number}"></script>  

        <link rel="stylesheet" href="static/css/bootstrap.min.css">

        <link rel="stylesheet" href="static/css/bootstrap-responsive.min.css">
		
        <link rel="stylesheet" href="static/css/styles.css">

		#* typekit *#
		<script type="text/javascript" src="//use.typekit.net/sgr1ljb.js"></script>
		<script type="text/javascript">try{Typekit.load();}catch(e){}</script>
		

</head>

    <body>
	
		<div class="navbar navbar-inverse navbar-fixed-top">
		 	#* empty nav for now *#
		 </div>
		<div class="container">
        	${body}

			#* bottom nav *#
			<div class="centered-pills">
				<ul class="nav nav-pills">
				#if $active_page == 'index'
				<li class="active">
				#else
				<li>
				#end if	
				    <a href="/">Home</a>
				</li>
							
				#if $active_page == 'accommodations'
				<li class="active">
				#else
				<li>
				#end if
					<a href="/accommodations">Accommodations</a>
				</li>
			
				#if $active_page == 'map'
				<li class="active">
				#else
				<li>
				#end if					
					<a href="/map">Map</a>
				</li>
				
				</ul>
				
				<ul class="nav nav-pills">
				
				#if $active_page == 'rsvp'
				<li class="active">
				#else
				<li>
				#end if					
					<a href="/rsvp">RSVP</a>
				</li>
				
				
				#if $active_page == 'gifts'
				<li class="active">
				#else
				<li>
				#end if					
					<a href="/gifts">Gifts</a>
				</li>
			
				</ul>
			</div>
		
		   <div class="inquiry_footer">
		      <a href="/contact">Other Inquiries</a>
		   </div>
		
		</div>
		
		
		
		
		<script type="text/javascript">

        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-39391560-1']);
        _gaq.push(['_trackPageview']);

        (function() {
          var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
          ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
          var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();

      </script>
		
    </body>
</html>