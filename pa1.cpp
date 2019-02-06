//Code That I have done at work to help make progress
//on PA1 when I don't have access to my computer.

//Helper to make a huffman tree.
//Outputs a hash table with the frequency of characters in the data.
unordered_map<char, int> mapCharFrequency(const vector<string> data)
{
    unordered_map<char, int> freqMap;
    
    for(auto str : data )
    {
        for(auto ch : str)
        {
            if(freqMap.find(ch) != freqMap.end())
            {
                //If character already exists increment the frequency of the character.
                freqMap[ch]++;
            }
            else
            {
                //Else insert into map with a value of 1.
                freqMap[ch] = 1;
            }
        }
    
    }
    
    return freqMap;
}

HuffmanTree<char>* PA1::huffmanTreeFromText(vector<string> data)
{

    //Builds a Huffman Tree from the supplied vector of strings.
    //This function implement's Huffman's Algorithm as specified in the
    //book.

    //In order for your tree to be the same as mine, you must take care 
    //to do the following:
    //1.	When merging the two smallest subtrees, make sure to place the 
    //      smallest tree on the left side!
	//store frequencies in hashtable
  
  unordered_map<char, int> dataFreqMap = mapCharFrequency(data);
  
	//maintains huffman tree forest 
    priority_queue < HuffmanTree<char>*, vector<HuffmanTree<char>*>, TreeComparer> forest{};
    
    for(auto h : dataFreqMap)
   {
      HuffmanTree<char> *node = new HuffmanTree(h.first, h.second);
      forest.push(node);
   }
   
   while(forest.size() >= 2)
   {
       HuffmanTree<char> *leftChild = forest.top();
       forest.pop()
       HuffmanTree<char> *rightChild = forest.top();
       
       if(leftChild.getWeight() > rightChild.getWeight())
       {
           leftChild = rightChild;
           rightChild = forest.top();
       }
       
       forest.pop();
       HuffmanTree *node = new HuffmanTree(leftChild, rightChild);
       forest.push(node);
       
   }
   
   
    //At this point only 1 tree should remain so we get it and return.
    return forest.top();
}
