$(document).ready(function(){	

		$('.slider').css('width', '100%').css('width', '-=160px');

		var element_meta = "<div class='element_block'><div class='upvote_block element upvote_e'> <div class='upvote_arrow element upvote_e'></div><div class='count element upvote_e'> 66 </div></div><div class='text'><a href='#' class='title element'> Title </a><a href='#' class='element discus_url'><img src='static/img/comment.png'  /><p class='comments_count'> 22 </p></a><br/><span class='description element opacity_link'> Description </span></div></div>"

		start_date = new Date(2013, 10, 25);
		currentDate  = new Date();

		var amountDates = Math.round( (currentDate - start_date) / 86400000 );

		var currentIndex = amountDates;

		for(var i = 0; i < amountDates+1; i++){

			var monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

			date = new Date();
			date.setDate( date.getUTCDate() - i );

			day = date.getUTCDate();
			month =  monthNames[date.getUTCMonth()];

			text = '<li><span class="date">' + day + '</span><span class="month">' + month + '</span></li>'

			$('#dates_bar').prepend(text);
		}

  
			$('#frame').sly({
				
				horizontal: 1,
	
				itemNav: 'basic',
				smart: 1,
				activateOn: 'click',
	
				scrollBy: 1,
	
				mouseDragging: 1,
				swingSpeed: 0.2,
	
				speed: 600,
				startAt: amountDates,

				prevPage: $('#arrow_left'), // Selector or DOM element for "previous page" button.
				nextPage: $('#arrow_right'), // Selector or DOM element for "next page" button.
			
			});
  

		function detailLoad(day, elem_index){

			$.get('detail', {day: day}, function(data){

				item_element_li = $('.slider .slider_item:eq(' + elem_index + ')');

				data = JSON.parse(data);

				length = data.length;

				if(length > 5){
					length = 5;
				}

				for(var i = 0; i < length; i++){

					item_element_li.append(element_meta);

					item_element = item_element_li.find('.element_block:last');

					votes_count = data[i]['votes_count'];
					name = data[i]['name'];
        			redirect_url = data[i]['redirect_url'];

        			discussion_url = data[i]['discussion_url'];
        			comments_count = data[i]['comments_count']

        			tagline = data[i]['tagline'];


        			item_element.find('.upvote_block .count').text(votes_count);

        			item_element.find('.title').text(name);
        			item_element.find('.title').attr('href', redirect_url);

        			item_element.find('.discus_url').attr('href', discussion_url);
        			item_element.find('.comments_count').text(comments_count);

        			item_element.find('.description').text(tagline);

        		}

            });

		}

		$('.content_arrow_right').click(function(){
			activateContent(currentIndex + 1);
		});


		$('.content_arrow_left').click(function(){
			activateContent(currentIndex - 1);
		});


		$('.dates_bar li').click(function(){		
			activateContent( $(this).index() );
		});

		function activateContent(index){

			if(index <= amountDates && index >= 0){

				currentIndex = index;

				test_item = $('.slider .slider_item:visible');

				// currentIndex
				// meta_index = amountDates - currentIndex;
				meta_index = currentIndex;

				detailLoad(meta_index, test_item.siblings().index() );

				test_item.fadeOut(300);
				test_item.siblings().fadeIn(300);

				test_item.empty();

				$('.date_bar_block .active').removeClass('active');
				$('.dates_bar li:eq(' + (currentIndex) +')' ).addClass('active');

				if(currentIndex == amountDates){ 
					$('.content_arrow_right img').css('opacity', '0.2'); 
					$('.content_arrow_right img').removeClass('active_arrow');
				}
				else{
				 	$('.content_arrow_right img').css('opacity', '1');   
					$('.content_arrow_right img').addClass('active_arrow');
				}

				if(index == 0){	
					$('.content_arrow_left img').css('opacity', '0.2'); 
					$('.content_arrow_left img').removeClass('active_arrow');
				}
				
				else{	
					$('.content_arrow_left img').css('opacity', '1'); 
					$('.content_arrow_left img').addClass('active_arrow');
				}

			}

		}

		activateContent(currentIndex);

});