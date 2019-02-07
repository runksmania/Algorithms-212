#include "PA1.h"

/// <summary>
/// Helper to make a huffman tree.
/// Maps the character frequency.
///Outputs a hash table with the frequency of characters in the data.
/// </summary>
/// <param name="data">Vector of strings, which needs its frequency of characters within all strings mapped</param>
/// <returns>Returns a hashTable with a int frequency of each character</returns>
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

/// <summary>
/// Builds a huffmans tree from a vector of strings.
/// </summary>
/// <param name="data">Vector of strings, which needs its frequency of characters within all strings mapped</param>
/// <returns>Returns a huffman tree with frequencies of each character in data.</returns>
HuffmanTree<char>* PA1::huffmanTreeFromText(vector<string> data)
{
    //Create data frequency map.
    unordered_map<char, int> dataFreqMap = mapCharFrequency(data);

    //maintains huffman tree forest 
    priority_queue < HuffmanTree<char>*, vector<HuffmanTree<char>*>, TreeComparer> forest{};

    for (auto kvp : dataFreqMap)
    {
        forest.push(new HuffmanTree<char>(kvp.first, kvp.second));
    }

    while (forest.size() >= 2)
    {
        //Get smallest and make it left child.
        HuffmanTree<char> *leftChild = forest.top();
        forest.pop();
        
        //Get next smallest and make it right child.
        HuffmanTree<char> *rightChild = forest.top();
        forest.pop();

        //Merge the trees.
        HuffmanTree<char> *node = new HuffmanTree<char>(leftChild, rightChild);
        forest.push(node);

    }


    //At this point only 1 tree should remain so we get it and return.
    return forest.top();
}

/// <summary>
/// Edits a huffman tree provided from calling function.
/// Adds characters at the locations symbolized by the binPathStr
/// </summary>
/// <param name="tree">A huffman tree node.</param>
/// <param name="ch">The character to insert into tree.</param>
/// <param name="binPathStr">The binary path for the character.</param>
void huffmanTreeFromMapHelper(HuffmanTree<char> *tree, char ch, string binPathStr)
{
    //Base case.
    if (binPathStr.size() < 1)
    {
        return;
    }

    if (tree == nullptr)
    {
        //If tree doesn't exist create it.
        tree = new HuffmanTree<char>(new HuffmanInternalNode<char>(nullptr, nullptr));
    }

    //Pointers to keep track of where we are.
    HuffmanNode<char> *previous = tree->getRoot();
    HuffmanNode<char> *current = previous;

    for (auto c : binPathStr)
    {
        //0 means go left, 1 means go right.
        if (c == '0')
        {
            current = current->getLeftChild();

            if (current == nullptr && c == binPathStr[binPathStr.size() - 1])
            {
                //If we are at the end and the leaf doesn't exist, create it.
                current = new HuffmanLeafNode<char>(ch, 0);
                previous->setLeftChild(current);
                return;
            }
            else if (current == nullptr)
            {
                //If we aren't at the end and the node doesn't exist, create an internal node.
                current = new HuffmanInternalNode<char>(nullptr, nullptr);
                previous->setLeftChild(current);
            }

            previous = current;

        }
        else if (c == '1')
        {
            current = current->getRightChild();

            if (current == nullptr && c == binPathStr[binPathStr.size() - 1])
            {
                //If we are at the end and the leaf doesn't exist, create it.
                current = new HuffmanLeafNode<char>(ch, 0);
                previous->setRightChild(current);
                return;
            }
            else if (current == nullptr)
            {
                //If we aren't at the end and the node doesn't exist, create an internal node.
                current = new HuffmanInternalNode<char>(nullptr, nullptr);
                previous->setRightChild(current);
            }

            previous = current;
        }
    }
}

/// <summary>
/// Creates a huffman tree from a huffman map.
/// </summary>
/// <param name="huffmanMap">huffman map.</param>
/// <returns>Returns a huffman tree created from the map given.</returns>
HuffmanTree<char>* PA1::huffmanTreeFromMap(unordered_map<char, string> huffmanMap)
{
    //Base case.
    if (huffmanMap.empty())
    {
        return nullptr;
    }

    //Create a new tree.
    HuffmanTree<char> *tree = new HuffmanTree<char>(new HuffmanInternalNode<char>(nullptr, nullptr));

    for (auto kvp : huffmanMap)
    {
        //Pass tree and each kvp to the helper function, which will add the kvp to the tree.
        huffmanTreeFromMapHelper(tree, kvp.first, kvp.second);
    }

    return tree;
}

/// <summary>
/// Helper function to make an encoding map from a huffman tree.
/// </summary>
/// <param name="map">The encoding map to change.</param>
/// <param name="node">A node of the huffman tree.</param>
/// <param name="encoding">The current encoding string path.</param>
void huffmanEncodingMapFromTreeHelper(unordered_map<char, string>& map, HuffmanNode<char>* node, string encoding)
{
    if (node->isLeaf() == false)
    {
        //If not a leaf make recursive calls.
        huffmanEncodingMapFromTreeHelper(map, node->getLeftChild(), encoding += '0');
        huffmanEncodingMapFromTreeHelper(map, node->getRightChild(), encoding  += '1');
        return;
    }
    else
    {
        //Else we have a complete mapping for character.
        map[node->getValue()] = encoding;
        return;
    }
}

/// <summary>
/// Creates and returns a encoding map from a huffman tree.
/// </summary>
/// <param name="tree">A huffman tree.</param>
/// <returns>Returns an encoding map of characters in the tree.</returns>
unordered_map<char, string> PA1::huffmanEncodingMapFromTree(HuffmanTree<char> *tree)
{
    unordered_map<char, string> result{};
    huffmanEncodingMapFromTreeHelper(result, tree->getRoot(), "");
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