

var UIController = (function(){

	var DOMstrings = {
		inputType: ".add__type",
		inputDescription : ".add__description",
		inputValue: ".add__value",
		inputButton:".add__btn",
		dateLabel: ".budget__title--month",

	}

	var nodeListForEach = function(list,callback){
				for(var i=0; i<list.length; i++){
					callback(list[i],i);
				}
			};
	
	return {
		
		displayDate:function(){

			var now,year,month,months,date,days,day;

			now = new Date();

			months = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim',
				'Kasım','Aralık']
			month  = now.getMonth();

			year =  now.getFullYear();

			document.querySelector(DOMstrings.dateLabel).textContent = months[month] + " " + year;

		},

		changedType : function(){

			var fields = document.querySelectorAll(
				DOMstrings.inputType + "," +
				DOMstrings.inputDescription + "," +
				DOMstrings.inputValue
				);

			nodeListForEach(fields,function(curr){
				curr.classList.toggle("red-focus");

			});

			var addBtn = document.querySelector(DOMstrings.inputButton)

			addBtn.classList.toggle('red');

		},

		getDomStrings : function(){
			return DOMstrings;
		},

		

		
	};
})();



//GLOBAL APP CONTROLLER
var controller = (function(UICtrl){

	 var setUpEventListener = function(){
		 var DOM = UICtrl.getDomStrings();

		 document.querySelector(DOM.inputType).addEventListener('change',UIController.changedType);

	 };
	

	 return{
	 	init: function(){
	 		setUpEventListener();
			UICtrl.displayDate();
	 		console.log('Application has started!');
	 		
	 	}
	 }
	 

})(UIController);


controller.init();