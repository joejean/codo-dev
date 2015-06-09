function Organizer(){
	var self = this;
	self.type = ko.observable("individual"),
	self.firstName = ko.observable('JoeTest');
	self.lastName = ko.observable('JeanTest');
	self.dob = ko.observable('1969-12-31');
	self.ssn = ko.observable('1234');
	self.country = ko.observable('US');
	self.street = ko.observable('14th Street');
	self.city = ko.observable('NY');
	self.state = ko.observable('NY');
	self.zipCode = ko.observable('10003');
	self.ip = ko.observable('207.251.103.46');
	self.managed = 'True';



	self.save= function(){
		url = "http://12.0.0.1:5000/organizer_signup";
		$.ajax("/organizer_signup",{
			type: "post",
			contentType: "application/json",
			data: ko.toJSON({
				type: self.type,
				first_name:self.firstName, 
				last_name: self.lastName, 
				dob:self.dob, 
				ssn: self.ssn, 
				country: self.country, 
				city: self.city, 
				state: self.state,
				street: self.street,
				ip: self.ip,
				managed: self.managed
			})
		});

	};

}

ko.applyBindings(new Organizer());
