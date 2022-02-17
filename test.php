<?php
class Chien {
    public $Nom;
    public $Age;
    public $Race;

    function __construct($Nom, $Age, $Race) {
        $this->Nom = $Nom;
        $this->Age = $Age;
        $this->Race = $Race;
    }
    function get_Nom() {
        return $this->Nom;
    }

    function get_Age() {
        return $this->Age;
    }

    function get_Race() {
        return $this->Race;
    }
}