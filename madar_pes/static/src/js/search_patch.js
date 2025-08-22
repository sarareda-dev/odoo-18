// /** @odoo-module **/

// import { patch } from "@web/core/utils/patch";
// import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

// console.log("POS custom search module loaded ✅");

// patch(ProductScreen.prototype, {
//     get productsToDisplay() {
//         const products = super.productsToDisplay;
//         const search = (this.searchWord || "").toLowerCase().trim();
//         // console.log(products)

//         // لما مفيش بحث: خزّن قائمة الأساس (حسب الكاتيجوري الحالي)
//         if (!search) {
//             this.__baseProducts = products;
//             return products;
//         }
//         // const allProducts = Object.values(this.env.services.pos.db.product_by_id || {});
//         console.log(this.env.services.pos_data.records['product.product'])
//         const productsMap = this.env.services.pos_data.records["product.product"];
//         const allProducts = Array.from(productsMap.values());

//         console.log("إجمالي المنتجات:", allProducts.length);
//         console.log("أول منتج:", allProducts[0]);
        

//         // استخدم قائمة الأساس إن وُجدت، وإلا fallback للي راجع (عشان أول مرة)
//         const base = this.__baseProducts || products;

//         // قسّم البحث لكلمات، وتجاهل الفراغات
//         const terms = search.split(/\s+/).filter(Boolean);

//         // AND + partial match على الاسم كله
//         const result = base.filter((p) => {
//             const name = (p.display_name || p.name || "").toLowerCase();
//             return terms.every((t) => name.includes(t));
//         });

//         return result;
//     },
// });



/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

patch(ProductScreen.prototype, {
    get productsToDisplay() {
        const search = (this.searchWord || "").toLowerCase().trim();

        // لو مفيش بحث → السلوك الأصلي
        if (!search) {
            return super.productsToDisplay;
        }

        // كل المنتجات من pos_data
        const allProducts = Array.from(
            this.env.services.pos_data.records["product.product"].values()
        );

        const terms = search.split(/\s+/).filter(Boolean);

        // بحث على: الاسم | الباركود | الكود الداخلي
        const result = allProducts.filter((p) => {
            const name = (p.display_name || p.name || "").toLowerCase();
            const barcode = (p.barcode || "").toLowerCase();
            const code = (p.default_code || "").toLowerCase();

            // شرط: أي كلمة من البحث تنطبق على أي حقل
            return terms.every(
                (t) =>
                    name.includes(t) ||
                    barcode.includes(t) ||
                    code.includes(t)
            );
        });

        return result;
    },
});


// /** @odoo-module **/

// import { patch } from "@web/core/utils/patch";
// import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

// console.log("✅ POS Custom Search Module Loaded for Odoo 18");

// patch(ProductScreen.prototype, {
//     get productsToDisplay() {
//         // الحصول على القائمة الأصلية
//         const originalProducts = super.productsToDisplay;
//         const search = (this.searchWord || "").toLowerCase().trim();

//         // لو ما في بحث → رجع القائمة العادية
//         if (!search) {
//             return originalProducts;
//         }

//         let allProducts = [];
//         let source = "unknown";

//         try {
//             if (this.env && this.env.pos) {
//                 if (this.env.pos.db && this.env.pos.db.product_by_id) {
//                     allProducts = Object.values(this.env.pos.db.product_by_id);
//                     source = "this.env.pos.db.product_by_id";
//                 } else if (this.env.pos.productDictionary) {
//                     allProducts = Object.values(this.env.pos.productDictionary);
//                     source = "this.env.pos.productDictionary";
//                 } else if (this.env.pos.products) {
//                     allProducts = this.env.pos.products;
//                     source = "this.env.pos.products";
//                 }
//             }
//         } catch (error) {
//             // console.error("❌ خطأ في جلب المنتجات:", error);
//             return originalProducts;
//         }

//         if (!allProducts.length) {
//             // console.warn("⚠️ لم يتم العثور على منتجات، إرجاع القائمة الأصلية");
//             return originalProducts;
//         }

//         // تقسيم الكلمات
//         const terms = search.split(/\s+/).filter(Boolean);

//         // فلترة المنتجات
//         const result = allProducts.filter((p) => {
//             const name = (p.display_name || p.name || "").toLowerCase();
//             const desc = (p.description || "").toLowerCase();
//             const barcode = (p.barcode || "").toLowerCase();
//             const defaultCode = (p.default_code || "").toLowerCase();

//             return terms.every((t) =>
//                 name.includes(t) ||
//                 desc.includes(t) ||
//                 barcode.includes(t) ||
//                 defaultCode.includes(t)
//             );
//         });

//         // Logging (لأغراض التصحيح)
//         console.groupCollapsed(`🔍 بحث POS: "${search}"`);
//         console.log(`📦 المصدر: ${source}, النتائج: ${result.length}`);
//         console.table(
//             result.map((p) => ({
//                 الاسم: p.display_name || p.name,
//                 الباركود: p.barcode,
//                 الكود: p.default_code,
//                 السعر: p.list_price,
//             }))
//         );
//         console.groupEnd();

//         return result;
//     },
// });
