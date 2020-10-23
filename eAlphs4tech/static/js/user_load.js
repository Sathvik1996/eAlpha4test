

    var count = 0;
    var str1 = 'http://ealpha4tech_systemtest.herokuapp.com/api/user_data/';
    var str2 = document.getElementById("myVar").value;
    var linkstr= str1.concat(str2);
    console.log(linkstr)


    $(document).ready(function() { fetchDataAndDisplay(); });

        function fetchDataAndDisplay(){
            $.ajax({
                url:linkstr,
                method:'GET'
            }).done(function(data){
                fLen = data['post_data_db_retrived'].length;
                console.log(data['user_name_disp']);
                document.getElementById('username_ajax').innerText= ('Welcome..! ').concat(String(data['user_name_disp']))
				
				// var csrf = "{% csrf_token %}";
				var str='';
				
				
                for (i = 0; i < fLen; i++) {
					var users = ''
					for (k=0;k<data['post_data_db_retrived'][i]['userdata'].length;k++){
						users+=
									"<span class='badge badge-success green_block tagedit'>" +
										"<p style='font-size: large;'>"+data['post_data_db_retrived'][i]['userdata'][k]+"</p>" +
									"</span>" 
					}
                    
					str+= 
				"<form id='formtoken' action='/userprofile' method='post'> " +

					"<header class=' text-white' style='padding-top: 40px; padding-bottom: 100px;'>" +
						"<div class='container text-center'>" +
						
					
						"<div class='card'>" +
							"<div class='card-header'>" +
								"<div class='row'>" +
								"<div class='col-sm'>" +
								"  <h4 style='color: darkred;'></h4>" +
								"</div>" +
								"<div class='col-sm'>" +
								"<h4 style='color: darkred;'>TASK</h4>" +
								"</div>" +
								"<div class='col-sm'>" +
								"<span class=' badge-success green_block'>" +
								"<h3 style='    " +
									"font-size: large;" +
									"background-color: #ffe3e3;" +
									"color: black;" +
									"padding-top: 3%;" +
									"padding-bottom: 3%;" +
									"font-weight: bold;" +
									"font-style: italic;'" +
								">Status :" +data['post_data_db_retrived'][i]['taskstatus'] + "</h3>" +
								"</span>" +
								"</div>" +
								"</div>" +
								"</div>" +
							
								"<div class='card-body'>" +
								"<h5 class='card-title'></h5>" +
								"<h5 class='card-text' style='font-weight: 700; color:black; padding-bottom:3%;'>" +
								data['post_data_db_retrived'][i]['task'] +
								"</h5>" +
					
								"<div class=''>" +
								"<div class='dists overflow-auto card-header' style='overflow-y: auto'>" +
								"<span class='badge'>" +
								"<p style='font-size: large; color: darkred;'>Users : </p>" +
								"</span>" + users +
								
									
								
									
								
								"</a>" +
								"</div>" +
								"</div>" +
								
								


								"<div class='card-header'>" +

								"<div class='row' style='padding-top: 2%;" +
								"padding-bottom: 2%;" +
												"background-color: #f5f7df; '>" +
												"<div class='col-2' style='padding-top:1%;'>" +
												"<p style='font-size: large; font-weight: bold;color: darkred;'>Update:</p>" +
												"</div>" +
								
												"<div class='col-8' style='padding-top:1%;'>" +
												"<div class='btn-group btn-group-toggle' data-toggle='buttons'>" +

												
												"<label class='btn btn-outline-info "+ data['post_data_db_retrived'][i]['checked_array'][0] + "'>" +
												"<input type='radio' class='Initiated' name='statusoptions' id='option1' value = 'Initiated$ "+data['post_data_db_retrived'][i]['task'] +"' autocomplete='off'> Initiated" +
												"</label>" +
												

												
												"<label class='btn btn-outline-secondary "+ data['post_data_db_retrived'][i]['checked_array'][1] + "'>" +
												"<input type='radio' class='In_Progress' name='statusoptions' id='option2' value='In_Progress$"+data['post_data_db_retrived'][i]['task'] +"' autocomplete='off' > In_Progress" +
												"</label>" +
												

												
												
												"<label class='btn btn-outline-success "+ data['post_data_db_retrived'][i]['checked_array'][2] + "'>" +
												"<input type='radio' class='Completed' name='statusoptions' id='option3' value='Completed$"+data['post_data_db_retrived'][i]['task'] +"' autocomplete='off' > Completed" +
												"</label>" +
												

												
												
												"<label class='btn btn-outline-danger "+ data['post_data_db_retrived'][i]['checked_array'][3] + "'>" +
												"<input type='radio' class='Delayed' name='statusoptions' id='option4' value='Delayed$"+data['post_data_db_retrived'][i]['task'] +"' autocomplete='off' > Delayed" +
												"</label>" +
												

												"</div>" +
												"</div>" +
												"<div class='col-2' >" +
												"<button type='submit' style='margin-top: 3%;' class='btn btn-primary btn-lg '>Submit</button>" +
												"</div>" +
												"</div>" +



												"</div>" +
												"</div>" +
						
					
							
					
					
					
												"</div>" +
												"</header>" +
					
					
					
												"</form>"
				}
				
		document.getElementById("unique_class_for_data").innerHTML = str ;
		document.getElementById("spinnercircle").style.display="None";
		
		})
	}

// <!-- ------------------------------------------------------------------------------------------------------------------------- -->