#include "PA1.h"

//Helper to make a huffman tree.
//Outputs a hash table with the frequency of characters in the data.
unordered_map<char, int> mapCharFrequency(const vector<string> data)
{
    unordered_map<char, int> freqMap;

    for (auto str : data)
    {
        for (auto ch : str)
        {
            if (freqMap.find(ch) != freqMap.end())
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

    for (auto h : dataFreqMap)
    {
        HuffmanTree<char> *node = new HuffmanTree<char>(h.first, h.second);
        forest.push(node);
    }

    while (forest.size() >= 2)
    {
        HuffmanTree<char> *leftChild = forest.top();
        forest.pop();
        HuffmanTree<char> *rightChild = forest.top();

        if (leftChild->getWeight() > rightChild->getWeight())
        {
            leftChild = rightChild;
            rightChild = forest.top();
        }

        forest.pop();
        HuffmanTree<char> *node = new HuffmanTree<char>(leftChild, rightChild);
        forest.push(node);

    }


    //At this point only 1 tree should remain so we get it and return.
    return forest.top();
}

//PA #1 TODO: Generates a Huffman character tree from the supplied encoding map
//NOTE: I used a recursive helper function to solve this!
HuffmanTree<char>* PA1::huffmanTreeFromMap(unordered_map<char, string> huffmanMap)
{
    //Generates a Huffman Tree based on the supplied Huffman Map.Recall that a 
    //Huffman Map contains a series of codes(e.g. 'a' = > 001).Each digit(0, 1) 
    //in a given code corresponds to a left branch for 0 and right branch for 1.
    return nullptr;
}

//PA #1 TODO: Generates a Huffman encoding map from the supplied Huffman tree
//NOTE: I used a recursive helper function to solve this!
unordered_map<char, string> PA1::huffmanEncodingMapFromTree(HuffmanTree<char> *tree)
{
    HuffmanNode<char> *node = tree->getRoot();
    if (node->isLeaf() == true)
    {
        HuffmanLeafNode<char> *leaf = dynamic_cast<HuffmanLeafNode<char> *>(node);
        leaf = (HuffmanLeafNode<char> *)node;
    }

    //Generates a Huffman Map based on the supplied Huffman Tree.  Again, recall 
    //that a Huffman Map contains a series of codes(e.g. 'a' = > 001).Each digit(0, 1) 
    //in a given code corresponds to a left branch for 0 and right branch for 1.  
    //As such, a given code represents a pre-order traversal of that bit of the 
    //tree.  I used recursion to solve this problem.
    unordered_map<char, string> result{};
    return result;
}

//PA #1 TODO: Writes an encoding map to file.  Needed for decompression.
void PA1::writeEncodingMapToFile(unordered_map<char, string> huffmanMap, string file_name)
{
    //Writes the supplied encoding map to a file.  My map file has one 
    //association per line (e.g. 'a' and 001 would yield the line "a001")
}

//PA #1 TODO: Reads an encoding map from a file.  Needed for decompression.
unordered_map<char, string> PA1::readEncodingMapFromFile(string file_name)
{
    //Creates a Huffman Map from the supplied file.Essentially, this is the 
    //inverse of writeEncodingMapToFile.  
    unordered_map<char, string> result{};
    return result;
}

//PA #1 TODO: Converts a vector of bits (bool) back into readable text using the supplied Huffman map
string PA1::decodeBits(vector<bool> bits, unordered_map<char, string> huffmanMap)
{
    //Uses the supplied Huffman Map to convert the vector of bools (bits) back into text.
    //To solve this problem, I converted the Huffman Map into a Huffman Tree and used 
    //tree traversals to convert the bits back into text.
    ostringstream result{};
    return result.str();
}

//PA #1 TODO: Using the supplied Huffman map compression, converts the supplied text into a series of bits (boolean values)
vector<bool> PA1::toBinary(vector<string> text, unordered_map<char, string> huffmanMap)
{
    vector<bool> result{};
    return result;
}