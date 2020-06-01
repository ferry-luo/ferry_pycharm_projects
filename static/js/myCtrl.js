// 通过 AngularJS 的 angular.module 函数来创建模块
var app = angular.module("myApp", []);
app.controller("myCtrl", function ($scope) {
    $scope.firstName = "John";
    $scope.lastName = "Doe";
});
