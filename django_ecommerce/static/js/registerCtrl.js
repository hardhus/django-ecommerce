mecApp.factory("UserFactory", function ($http) {
    var factory = {};
    factory.register = function (user_data) {
        return $http.post("/register/", user_data).then(function (response) {
            return response.data;
        });
    };
    return factory;
});

mecApp.controller("RegisterCtrl", function ($scope, $http, UserFactory) {
    var logRegisterErrors = function (errors) {
        $scope.register_errors = errors;
    };

    var redirect_to_user_page = function (response) {
        if (response.errors) {
            throw response.errors;
        } else {
            window.location = response.url;
        }
    };

    $scope.register = function () {
        $scope.register_errors = "";

        user_data = {
            name: $scope.user_form.name.$modelValue,
            email: $scope.user_form.email.$modelValue,
            password: $scope.user_form.password.$modelValue,
            password2: $scope.user_form.ver_password.$modelValue,
        };
        console.log(user_data);
        UserFactory.register($scope.user_form)
            .then(redirect_to_user_page)
            .then(null, logRegisterErrors);
    };
});
