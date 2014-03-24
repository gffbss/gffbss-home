/*
      // Function for intro
      $('.enter_btn').on('click',function(){
        $('.enter').addClass('showme');

        $('.enter_btn').animate({top: '-200%'},500);
        $('.divider').delay(20).animate({left: '-200%'},800);
        $('.copyright').delay(30).animate({right: '-200%'},700);

        var time = setTimeout(function(){
          $('.enter').addClass('hideme');
          $('body').css('overflow','auto');
          clearTimeout(time);
        },2000);
      });
*/

// js.run();
var js = (function(){

  //  strict mode
  'use strict';

  // return functions
  return {

    // Call functions here
    run: function(){
      this.fns();
      this.Copyright();
    },

    // run with this.debug(foo);
    debug: function(el){
      if(typeof console != 'undefined')
        if(this.info.debug){console.clear();console.log('%c'+el,'color:blue;');}
        else{console.clear();}
    },

    // functions
    fns: function(){
      // Function for intro
      $('.enter_btn').on('click',function(){
        $('.enter').addClass('showme');

        $('.enter_btn').animate({top: '-200%'},500);
        $('.divider').delay(20).animate({left: '-200%'},800);
        $('.copyright').delay(30).animate({right: '-200%'},700);

        var time = setTimeout(function(){
          $('.enter').addClass('hideme');
          $('body').css('overflow','auto');
          clearTimeout(time);
        },2000);
      });

    },


    // Show info in console log
    Copyright: function(){
      // info template
       var copyright = 'Author: '+ this.info.author + '\n'+
          'Description: ' + this.info.description + '\n'+
          'Date: ' + this.info.date + '\n'+
          'Url: ' + this.info.url;
      // run in console.log
      this.debug(copyright);
    }

  }; // end of return

}).call(this);

// Call functions
js.run();
/**
 * Created by geoffreyboss on 3/23/14.
 */
