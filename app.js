var main = function () {
    
    $('.arrow-next').click(function() {
        var currentSlide = $('.active-slide');
        var nextSlide= $('.active-slide').next();
        var currentDot = $('.active-dot');
        var nextDot= $('.active-dot').next();
        if(nextSlide.length == 0) {
			nextSlide = $('.slide').first();
			nextDot = $('.dot').first();
		}
        currentSlide.fadeOut(600);
        currentSlide.removeClass('active-slide');
        nextSlide.fadeIn(600);
        nextSlide.addClass('active-slide');
        currentDot.removeClass('active-dot');
        nextDot.addClass('active-dot');
    });
	
    $('.arrow-prev').click(function() {
        var currentSlide = $('.active-slide');
        var prevSlide= $('.active-slide').prev();
        var currentDot = $('.active-dot');
        var prevDot= $('.active-dot').prev();
        if(prevSlide.length == 0) {
    prevSlide = $('.slide').last();
    prevDot = $('.dot').last();
  }
        currentSlide.fadeOut(600);
        currentSlide.removeClass('active-slide');
        prevSlide.fadeIn(600);
        prevSlide.addClass('active-slide');
        currentDot.removeClass('active-dot');
        prevDot.addClass('active-dot');
    });
};

$(document).ready(main);