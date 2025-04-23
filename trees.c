
#include <stdlib.h>
#include <iostream.h>



 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };
 
class Solution {
public:
    void createParentNode(unordered_map<TreeNode*, TreeNode*> &umap,
                          TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        umap[root] = NULL;
        while (!q.empty()) {
            TreeNode* frontnode = q.front();
            q.pop();
            if (frontnode->left) {
                umap[frontnode->left] = frontnode;
                q.push(frontnode->left);
            }
            if (frontnode->right) {
                umap[frontnode->right] = frontnode;
                q.push(frontnode->right);
            }
        }
        return;
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        vector<int> ans;
        if (root == NULL)
            return ans;
        unordered_map<TreeNode*, TreeNode*> parentmap;
        createParentNode(parentmap, root);
        unordered_map<TreeNode*, bool> visited;
        visited[target] = true;
        queue<TreeNode*> q;
        q.push(target);
        int level = 0;
        while (!q.empty()) {
            if (level == k)
                break;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* frontnode = q.front();
                q.pop();
                if (frontnode->left && !visited[frontnode->left]) {
                    q.push(frontnode->left);
                    visited[frontnode->left] = true;
                }
                if (frontnode->right && !visited[frontnode->right]) {
                    q.push(frontnode->right);
                    visited[frontnode->right] = true;
                }
                if (parentmap[frontnode] && !visited[parentmap[frontnode]]) {
                    q.push(parentmap[frontnode]);
                    visited[parentmap[frontnode]] = true;
                }
            }

            level += 1;
        }
       
        while(!q.empty()){
            ans.push_back(q.front()->val);
            q.pop();
        }
        return ans;
    }
};