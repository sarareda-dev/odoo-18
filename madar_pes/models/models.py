import logging
from odoo import models, fields, api
from odoo.osv import expression
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = "product.template"

    token_search = fields.Char(
        string="Tokenized Search",
        compute="_compute_token_search",
        search="_search_token_search",
        store=False,
    )

    def _compute_token_search(self):
        for record in self:
            record.token_search = False  # حقل حسابي فقط للبحث

    def _search_token_search(self, operator, value):
        _logger.info("🔍 Tokenized Search Triggered - Operator: %s, Value: %s", operator, value)
        
        if not value:
            return []
        
        tokens = value.split()
        domain = []
        for token in tokens:
            token_domain = ["|", "|", ("name", "ilike", token), ("default_code", "ilike", token),("barcode", "ilike", token)]
            if domain:
                domain = ["&"] + domain + token_domain
            else:
                domain = token_domain

        _logger.info("✅ Final Search Domain: %s", domain)
        return domain
    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        # Logging for tracking
        _logger.info("Function name_search called.")
        _logger.info("Search Query: %s", name)
        _logger.info("Initial arguments: %s", args)

        args = args or []
        if name:
            _logger.info("Query name is not empty. Proceeding with custom search logic.")
            
            # Split the search query into words
            words = name.split()
            _logger.info("Words in the query: %s", words)
            
            # Build domain conditions for each word
            domain = []
            for word in words:
                domain.append(('name', operator, word))
            
            _logger.info("Constructed domain list: %s", domain)

            # Combine word conditions with AND
            if domain:
                if len(domain) > 1:
                    name_domain = ['&'] * (len(domain) - 1) + domain
                else:
                    name_domain = domain
                
                _logger.info("Combined name_domain: %s", name_domain)
                
                # Combine with the original arguments using AND
                final_domain = args + name_domain
                _logger.info("Final search arguments: %s", final_domain)
                
                return super(ProductTemplate, self).name_search('', args=final_domain, operator=operator, limit=limit)

        _logger.info("Query name is empty. Returning all records with initial arguments.")
        return super(ProductTemplate, self).name_search(name, args=args, operator=operator, limit=limit)


class ProductProduct(models.Model):
    _inherit = "product.product"
    
    
    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        # Logging for tracking
        _logger.info("Function name_search called.")
        _logger.info("Search Query: %s", name)
        _logger.info("Initial arguments: %s", args)

        args = args or []
        if name:
            _logger.info("Query name is not empty. Proceeding with custom search logic.")
            
            # Split the search query into words
            words = name.split()
            _logger.info("Words in the query: %s", words)
            
            # Build domain conditions for each word
            domain = []
            for word in words:
                domain.append(('name', operator, word))
            
            _logger.info("Constructed domain list: %s", domain)

            # Combine word conditions with AND
            if domain:
                if len(domain) > 1:
                    name_domain = ['&'] * (len(domain) - 1) + domain
                else:
                    name_domain = domain
                
                _logger.info("Combined name_domain: %s", name_domain)
                
                # Combine with the original arguments using AND
                final_domain = args + name_domain
                _logger.info("Final search arguments: %s", final_domain)
                
                return super(ProductProduct, self).name_search('', args=final_domain, operator=operator, limit=limit)

        _logger.info("Query name is empty. Returning all records with initial arguments.")
        return super(ProductProduct, self).name_search(name, args=args, operator=operator, limit=limit)