local vim = vim

-- Install lazy.nvim if not already installed
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git", "--branch=stable", lazypath
  })
end
vim.opt.rtp:prepend(lazypath)

-- Load plugins
require("lazy").setup({
  { "AlphaTechnolog/pywal.nvim", lazy = false, priority = 1000 },
  { "NvChad/nvim-colorizer.lua", config = function()
      require("colorizer").setup({
        "*", -- Enable for all file types
        css = { rgb_fn = true }, -- Enable rgb() function support in CSS
        html = { names = true }  -- Enable color name support (e.g., "red", "blue")
      })
    end 
  },

  { "nvim-lualine/lualine.nvim", dependencies = { "nvim-tree/nvim-web-devicons" } },
  { "nvim-telescope/telescope.nvim", dependencies = { "nvim-lua/plenary.nvim" } },
  { "neovim/nvim-lspconfig" },
  { "Exafunction/codeium.vim" },
  { "hrsh7th/nvim-cmp", dependencies = { "hrsh7th/cmp-nvim-lsp", "L3MON4D3/LuaSnip" } },
  { "goolord/alpha-nvim", dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      local alpha = require("alpha")
      local dashboard = require("alpha.themes.dashboard")

      -- Set header
      dashboard.section.header.val = {
        "   ██████╗ ███╗   ███╗██╗  ██╗ ",
        "  ██╔════╝ ████╗ ████║██║  ██║ ",
        "  ██║  ███╗██╔████╔██║███████║ ",
        "  ██║   ██║██║╚██╔╝██║██╔══██║ ",
        "  ╚██████╔╝██║ ╚═╝ ██║██║  ██║ ",
        "   ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝ ",
        "         Forever, always."
      }

      -- Set menu buttons
      dashboard.section.buttons.val = {
        dashboard.button("n", "  New file", ":ene <BAR> startinsert <CR>"),
        dashboard.button("f", "  Find file", ":Telescope find_files hidden=true<CR>"),
        dashboard.button("r", "  Recent files", ":Telescope oldfiles<CR>"),
        dashboard.button("e", "  Edit Qtile", ":e ~/.config/qtile/config.py<CR>"),
        dashboard.button("t", "󱠓  Edit Themes", ":e ~/.config/qtile/themes/theme.py<CR>"),
        dashboard.button("c", "  Configuration", ":e ~/.config/nvim/init.lua<CR>"),
        dashboard.button("q", "  Quit Neovim", ":qa<CR>"),
      }

      -- Apply layout
      alpha.setup(dashboard.config)
    end 
  },
  {
    "kyazdani42/nvim-tree.lua",
    config = function()
      require("nvim-tree").setup({
        -- Add your preferred nvim-tree settings here
        disable_netrw = true,  -- Disable netrw so nvim-tree takes over
        hijack_netrw = true,   -- Hijack netrw to open nvim-tree by default
        open_on_tab = false,   -- Disable automatic opening on new tab
        view = {
          width = 30,  -- Width of the file tree
          side = "left",  -- Position of the file tree
        },
      })
    end }
  })


-- Enable system clipboard access
vim.opt.clipboard = "unnamedplus"

-- Keybinding for Select All
vim.api.nvim_set_keymap("n", "<C-a>", "ggVG", { noremap = true, silent = true }) -- Ctrl + A to select all text in normal mode

-- Keybinding for Copy (Ctrl + C)
vim.api.nvim_set_keymap("n", "<C-c>", '"+y', { noremap = true, silent = true }) -- Ctrl + C to copy selected text to the system clipboard

-- Keybinding for Paste (Ctrl + P)
vim.api.nvim_set_keymap("n", "<C-p>", '"+p', { noremap = true, silent = true }) -- Ctrl + P to paste from the system clipboard
 
-- Keybindings for switching buffers
vim.api.nvim_set_keymap("n", "<Tab>", ":BufferLineCycleNext<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<S-Tab>", ":BufferLineCyclePrev<CR>", { noremap = true, silent = true })

  -- Ensure this closing bracket exists to properly terminate `lazy.setup()`
vim.api.nvim_set_keymap("n", "<Space>e", ":NvimTreeToggle<CR>", { noremap = true, silent = true })
-- Set colorscheme
vim.cmd.colorscheme("pywal")

-- Remove tildes (~) on empty lines
vim.opt.fillchars = { eob = " " }
vim.opt.swapfile = false

-- Enable line numbers
vim.opt.number = true
vim.opt.relativenumber = true

vim.g.codeium_enabled = true  -- Enable Codeium AI
vim.g.codeium_completion_enabled = true  -- Enable code completion

-- Optional: Set your own key mapping for accepting AI suggestions
vim.api.nvim_set_keymap("i", "<Tab>", 'codeium#Accept()', { expr = true, noremap = true })

-- Lualine setup


-- LSP setup
local lspconfig = require("lspconfig")
lspconfig.lua_ls.setup({})
lspconfig.pyright.setup({})
lspconfig.ts_ls.setup({})

-- Completion setup
local cmp = require("cmp")
cmp.setup {
  mapping = {
    ["<C-Space>"] = cmp.mapping.complete(),
    ["<CR>"] = cmp.mapping.confirm({ select = true })
  },
  sources = cmp.config.sources({
    { name = "nvim_lsp" },
    { name = "luasnip" }
  })
}

require('lualine').setup {
  options = {
    theme = 'auto',  -- Change to your preferred theme
  },
  sections = {
    lualine_b = {'branch', 'diff', 'diagnostics'},
    lualine_c = {'filename'},
    lualine_x = {'encoding', 'fileformat', 'filetype'},
    lualine_y = {'progress'},
    lualine_z = {'location'}
  },
}

-- Close nvim-tree when opening a file
vim.api.nvim_create_autocmd("BufEnter", {
  pattern = "*",
  callback = function()
    if not vim.api.nvim_buf_get_option(0, "buftype") == "nofile" then
      require("nvim-tree").close()
    end
  end,
})


-- Telescope configuration to show dotfiles
require("telescope").setup {
  defaults = {
    file_ignore_patterns = {},
    vimgrep_arguments = {
      "rg", "--color=never", "--no-heading", "--with-filename", "--line-number", "--column",
      "--smart-case", "--hidden"
    }
  }
}
vim.api.nvim_set_keymap("n", "<leader>fd", ":Telescope find_files hidden=true<CR>", { noremap = true, silent = true })
