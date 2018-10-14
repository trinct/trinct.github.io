pragma solidity ^0.4.0;
contract One{
    struct AAA{
        string CountryName;
        string CountryCode;
    }
    
    struct BBB{
        string Year;
        string MetricTon;
    }
    
    mapping(address=>BBB) public DataList;
    mapping(address=>AAA) public CountryList;
    
    constructor() public{
        
    }
    
    function AddCountry(string _name,string _code) public
    {
        CountryList[msg.sender] = AAA(_name,_code);
    }
    
    function AddData(string _year,string _metricTon) public
    {
        DataList[msg.sender] = BBB(_year,_metricTon);
    }
    
    function GetCountry() view public returns(string,string)
    {
        return(CountryList[msg.sender].CountryName,CountryList[msg.sender].CountryCode);
    }
    
    function GetData() view public returns(string,string)
    {
        return(DataList[msg.sender].Year,DataList[msg.sender].MetricTon);
    }
}
