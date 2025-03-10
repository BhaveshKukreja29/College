// Write a program to simulate LRU page replacement techniques
// we will replace the one that was used long time ago

//take input of frames
// take string of requests

// each page is a struct with attributes as time spent in memory
// frames is a struct array containing the element 

// have an output array of string showing hit or miss

// algorithm is to iterate over each frame element and check which element is in it.
// if there is no element matching to our request we swap the one with most time spent in memory
// after swap we have to keep the new time spent as 0

// after every request, we will increment the time spent of every process
