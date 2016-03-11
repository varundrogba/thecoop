$(document).ready(function()
	{
		$("#loginbutton").click(function()
		{
    		$.ajax(
    		{
    				url: "/login/",
    				success: function()
	    			{
	        			alert('ajax call');
	    			},		
					error: function()
					{
						alert('error!');
					}
			}
			);
		}
		);
	});	


$(document).ready(function()
	{
    	$.ajax(
    		{
    				url: 'http://127.0.0.1:8000/api/thecoop_api/event/',
    				type: 'GET',
  					contentType: 'application/json',
  					//data: data,
  					dataType: 'json',
  					processData: false,
    				success: function(data)
	    			{
	        			$("#no_of_active_events").text(data.meta.total_count);
	    			},		
					error: function()
					{
						alert('Unable to load event information');
					}
			}
			);
	});	
